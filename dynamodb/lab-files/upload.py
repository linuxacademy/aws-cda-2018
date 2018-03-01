# There are some issues in this code. 
# Time for you to fix them and get that 
# data where it needs to go!

import boto3
import json

dynamodb = boto3.client('dynamodb')

def upload():
    with open('songs.json', 'r') as songfile:
        songs = json.load(songfile)
    for song in songs:
        response = dynamodb.put_item(
            TableName='aTable?', 
            Item={
                'Artist':{'A':song['Artist']},
                'SongTitle':{'S':song['SongTitle']},
                'price':{'P': song['price']},
                'studio':{'S': song['studio']},
                'address':{'A': song['address']}
            }
        )
        print(response)

the_uploader()