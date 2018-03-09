import boto3
import time
from sqs_url import QUEUE_URL

sqs = boto3.client('sqs')

i = 0 

while i < 100000:
    i = i + 1
    time.sleep(1)
    response = sqs.get_queue_attributes(
        QueueUrl=QUEUE_URL,
        AttributeNames=[
            'ApproximateNumberOfMessages',
            'ApproximateNumberOfMessagesNotVisible',
            'ApproximateNumberOfMessagesDelayed',
        ]
    )
    for attribute in response['Attributes']:
        print(
            response['Attributes'][attribute] + 
            ' ' + 
            attribute
        )
    print('')
    print('')
    print('')
    print('')

