import boto3
import json

dynamodb = boto3.client('dynamodb')

print('Query Local Index:')
q_res=dynamodb.query(
    TableName="MusicTwo",
    IndexName="MusicTwo",
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL',
    ExpressionAttributeValues={
        ":p_key":{"S":"Anthony Haslett"},
        ":s_key":{"S":"December Lavender"}
    },
    KeyConditionExpression='Artist = :p_key AND SongTitle = :s_key'
)

print(q_res)

print('Query Global Index:')