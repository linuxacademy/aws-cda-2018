import boto3

VERIFIED_EMAIL = 'YOUR_SES_VERIFIED_EMAIL'

ses = boto3.client('ses')

def handler(event, context):
    data = json.loads(event['body'])
    ses.send_email(
        Source=VERIFIED_EMAIL,
        Destination={
            'ToAddresses': data['email']  # Also a verified email
        },
        Message={
            'Subject': {'Data': 'A reminder from your reminder service!'},
            'Body': {'Text': {'Data': reminder}}
        }
    )
    return 'Success!'