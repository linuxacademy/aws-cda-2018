import boto3
import json
import time
from sqs_url import QUEUE_URL

# Create SQS client
sqs = boto3.client('sqs')

with open('slow_data.json', 'r') as f:
    data = json.loads(f.read())

for i in data:
    msg_body = json.dumps(i)
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=msg_body,
        DelaySeconds=10,
        MessageAttributes={
            'JobType': {
                'DataType': 'String',
                'StringValue': 'NewDonor'
            },
            'Producer': {
                'DataType': 'String',
                'StringValue': 'Slow'
            }
        }
    )
    print('Added a message with 10 second delay - SLOW')
    print(response)
    time.sleep(1)
