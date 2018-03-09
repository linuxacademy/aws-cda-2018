import boto3
import json
import time
from sqs_url import QUEUE_URL

# Create SQS client
sqs = boto3.client('sqs')

response = sqs.receive_message(
    QueueUrl=QUEUE_URL,
    MessageAttributeNames=[
        'All',
    ],
    MaxNumberOfMessages=1,
    VisibilityTimeout=5,
    WaitTimeSeconds=10
)