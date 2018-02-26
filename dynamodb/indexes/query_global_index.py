import boto3
import json

dynamodb = boto3.client('dynamodb')


print('Query Global Index:')
q_res=dynamodb.query(
    TableName="MusicTwo",
    IndexName="studio-price-index",   
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL',
    ExpressionAttributeValues={
        ":p_key":{"S":"GEEKWAGON"},
        ":s_key":{"N":"10"}
    },
    KeyConditionExpression='studio = :p_key AND price > :s_key'
)