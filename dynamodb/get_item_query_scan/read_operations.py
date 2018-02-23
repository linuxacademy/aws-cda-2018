import boto3
import json

dynamodb = boto3.client('dynamodb')

def upload():
    with open('songs.json', 'r') as songfile:
        songs = json.load(songfile)
    for song in songs:
        response = dynamodb.put_item(
            TableName='Music', 
            Item={
                'Artist':{'S':song['Artist']},
                'SongTitle':{'S':song['SongTitle']},
                'price':{'S': song['price']},
                'studio':{'S': song['studio']},
                'address':{'S': song['address']}
            }
        )
        print("UPLOADING ITEM")
        print(response)

upload()

# Item we want:
# {
#     "Artist": "Anthony Haslett",
#     "SongTitle": "December Lavender",
#     "price": "$1.05",
#     "studio": "PHOTOBIN",
#     "address": "886 Locust Avenue, Suitland, Vermont, 8689"
# },

print('GetItem:')
dynamodb.get_item(
    TableName='Music', 
    Key={
        'Artist':{'S':"Anthony Haslett"},
        'SongTitle':{'S':"December Lavender"}
    },
    ReturnConsumedCapacity='TOTAL'
)


print('Query:')
dynamodb.query(
    TableName="Music",
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL',
    ExpressionAttributeValues={
        ":p_key":{"S":"Anthony Haslett"},
        ":s_key":{"S":"December Lavender"}
    },
    KeyConditionExpression='Artist = :p_key AND SongTitle = :s_key'
)


dynamodb.query(
    TableName="Music",
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL',
    ExpressionAttributeValues={
        ":p_key":{"S":"Anthony Haslett"},
        ":num":{"S":"19"}
    },
    KeyConditionExpression='Artist = :p_key',
    FilterExpression='contains(price, :num)'
)


print('Scan:')
dynamodb.scan(
    TableName="Music",
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='TOTAL',
    ExpressionAttributeValues={
        ":p_key":{"S":"Anthony Haslett"},
        ":s_key":{"S":"December Lavender"}
    },
    FilterExpression='Artist = :p_key AND SongTitle = :s_key'
)