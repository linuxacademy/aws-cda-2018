import boto3

sns = boto3.client('sns')

def handler(event, context):
    data = json.loads(event['body'])
    sns.publish(PhoneNumber=data['phone'], Message=data['message'])
    return 'Success!'