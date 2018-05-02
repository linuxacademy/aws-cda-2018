import boto3
import json
import os

SFN_ARN = 'YOUR_ARN_HERE'

sfn = boto3.client('stepfunctions')

def handler(event, context):
    print('EVENT:')
    print(event)
    data = json.loads(event['body'])

    # Validation Checks
    checks = []
    checks.append('waitSeconds' in data)
    checks.append(type(data['waitSeconds']) == int)
    checks.append('preference' in data)
    if data.get('preference') == 'sms':
        checks.append('phone' in data)
    if data.get('preference') == 'email':
        checks.append('email' in data)

    # Check for any errors in validation checks
    if False in checks:
        response = {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": json.dumps({
                "Status": "Success", 
                "Reason": "Input failed validation"
            })
        }
    else: 
        sfn.start_execution(
            stateMachineArn=SFN_ARN,
            input=data
        )
        response = {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin":"*"},
            "body": json.dumps({
                "Status": "Success"
            })
        }
    return response