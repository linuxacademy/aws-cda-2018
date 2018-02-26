import boto3

dynamodb = boto3.client('dynamodb')


print('Query Global Index:')
q_res=dynamodb.query(
    TableName="MusicTwo",
    IndexName="studio-price-index",   
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL',
    ExpressionAttributeValues={
        ":p_key":{"S":"SLAX"},
        ":s_key":{"S":"10"}
    },
    KeyConditionExpression='studio = :p_key AND price > :s_key'
)
print(q_res)