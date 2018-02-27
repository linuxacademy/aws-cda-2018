import boto3

dynamodb = boto3.client('dynamodb')

print("Atomic Counter:")
response = dynamodb.update_item(
    TableName='MusicThree', 
    Key={
        'Artist':{'S': "Anthony Haslett"},
        'SongTitle':{'S':"Ivory Maroon"}
    },
    UpdateExpression='SET price = price + :inc',
    ExpressionAttributeValues={
        ':inc': {'N': '1'}
    },
    ReturnValues="UPDATED_NEW"
)
print("UPDATING ITEM")
print(response)

