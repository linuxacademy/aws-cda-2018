import boto3
import json
import time
from sqs_url import QUEUE_URL

# Create SQS client
sqs = boto3.client('sqs')

i = 0

while i < 10000:
    i = i + 1
    rec_res = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MessageAttributeNames=[
            'All',
        ],
        MaxNumberOfMessages=1,
        VisibilityTimeout=20,
        WaitTimeSeconds=10
    )
    del_res = sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=rec_res['Messages'][0]['ReceiptHandle']
    )
    print("RECIEVED MESSAGE (SLOW CONSUMER):")
    print('FROM PRODUCER: ' + rec_res['Messages'][0]['MessageAttributes']['Producer']['StringValue'])
    print('JOB TYPE: ' + rec_res['Messages'][0]['MessageAttributes']['JobType']['StringValue'])
    print('BODY: ' + rec_res['Messages'][0]['Body'])
    print("DELETED MESSAGE (SLOW CONSUMER)")
    print("")
    time.sleep(8)