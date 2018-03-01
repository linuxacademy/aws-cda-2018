# There are some issues in this code. 
# I left a few comments to help you fix it while I'm on vacation

import boto3
import json

dynamodb = boto3.client('dynamodb')

def upload():
    with open('songs.json', 'r') as songfile:
        songs = json.load(songfile)
    for song in songs:
        response = dynamodb.put_item(
            # What was the table name? Can't remember.
            TableName='aTable?', 
            Item={
                # Pretty sure I need to clean up some data types here
                'Artist':{'A':song['Artist']},
                'SongTitle':{'S':song['SongTitle']},
                'price':{'P': song['price']},
                'studio':{'S': song['studio']},
                'address':{'A': song['address']}
            }
        )
        print(response)

upload()