import boto3
import csv 
import json

s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

def handler(event, context):
    # Get the object from the event then download it to Lambda tmp space
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    # IMPORTANT:
    if '.csv' not in key:
        return 'Not a csv that needs processing'
    if '.psv' in key:
        return 'An already processed logfile'
    s3.download_file(bucket, key, '/tmp/' + key)
    psv_name = 'processed_' + key[0:-4] + '.psv'
    # Open the file, process it, and upload a psv
    with open('/tmp/' + key, 'r') as infile, \
         open('/tmp/' + psv_name, 'w') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, reader.fieldnames, delimiter='|')
        writer.writeheader()
        writer.writerows(reader)
    s3.upload_file('/tmp/' + psv_name, bucket, psv_name)
    # Use DynamoDB atomic counters to tally visits in csv
    with open('/tmp/' + key, 'r') as infile:
        for row in infile:
            ddb_key = row.strip().split(',')[0]
            ddb_inc = row.strip().split(',')[1]
            if 'site' not in ddb_key:
                response = dynamodb.update_item(
                    TableName='siteVisits', 
                    Key={
                        'siteUrl':{'S': ddb_key}
                    },
                    UpdateExpression='ADD visits :inc',
                    ExpressionAttributeValues={
                        ':inc': {'N': ddb_inc}
                    },
                    ReturnValues="UPDATED_NEW"
                )
                print(response)