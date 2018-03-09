import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='mynewq.fifo',
    Attributes={
        'DelaySeconds': '5',
        'MessageRetentionPeriod': '86400',
        'FifoQueue': 'true',
        'ContentBasedDeduplication': 'true'
    }
)

print(response['QueueUrl'])