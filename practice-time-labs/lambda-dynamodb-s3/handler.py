import boto3
import csv 
import json

s3 = boto3.client('s3')

def handler(event, context):
    # Get the object from the event then download it to Lambda tmp space
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
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
