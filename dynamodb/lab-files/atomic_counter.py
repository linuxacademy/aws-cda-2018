import boto3

dynamodb = boto3.client('dynamodb')

print("Atomic Counter:")
response = dynamodb.update_item(
    TableName='whatisthis_silly_tablename?',  # better update this
    Key={
        'Artist':{'N': "Anthony Haslett"},  # I think I might have messed up here
        'SongTitle':{'N':"Ivory Maroon"}
    },
    UpdateExpression='SET price = price + :inc',
    ExpressionAttributeValues={
        ':inc': {'N': ''}  # let's try incrementing by 3?
    },
    ReturnValues="UPDATED_NEW"
)
print("UPDATING ITEM")
print(response)

