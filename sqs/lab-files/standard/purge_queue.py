import boto3
from sqs_url import QUEUE_URL

sqs = boto3.client('sqs')

response = sqs.purge_queue(
    QueueUrl=QUEUE_URL
)