import boto3
import json

dynamodb = boto3.client('dynamodb')

print('Query Local Index:')
q_res=dynamodb.query(
    TableName="MusicTwo",
    IndexName="Artist-price-index",   
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL',
    ExpressionAttributeValues={
        ":p_key":{"S":"Anthony Haslett"},
        ":s_key":{"S":"15"}
    },
    KeyConditionExpression='Artist = :p_key AND price > :s_key'
)
