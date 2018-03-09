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
        VisibilityTimeout=5,
        WaitTimeSeconds=10
    )
    print(rec_res)
    # If our task takes too long we can't delete it
    # time.sleep(5)
    del_res = sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=rec_res['Messages'][0]['ReceiptHandle']
    )
    print("DELETED:")
    print(del_res)
    time.sleep(5)