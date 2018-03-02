import boto3

dynamodb = boto3.client('dynamodb')

print("Conditional Write:")
response = dynamodb.update_item(
    TableName='someTableNameIthink',  # oops! Better fix this
    Key={
        'Artist':{'S': "Anthony Haslett"},
        'SongTitle':{'S':"Blue Magenta"}
    },
    UpdateExpression='SET price = :val',
    ExpressionAttributeValues={
        ':val': {'N': '15.37'},  # Make sure we keep this line the same
        ':currval': {'N': '1.2345'}  # What was the current value?
    },
    ConditionExpression='price = :currval',
    ReturnValues="ALL_NEW"
)
