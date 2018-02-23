import boto3
import json

dynamodb = boto3.client('dynamodb')

def write(artist, song_title, price, studio, address):
    response = dynamodb.put_item(
        TableName='Music', 
        ReturnConsumedCapacity='TOTAL',
        Item={
            'Artist':{'S':artist},
            'SongTitle':{'S':song_title},
            'price':{'S': price},
            'studio':{'S': studio},
            'address':{'S': address}
        }
    )
    print(response)

def delete(artist, song_title):
    response = dynamodb.delete_item(
        TableName='Music', 
        ReturnConsumedCapacity='TOTAL',
        Key={
            'Artist':{'S':artist},
            'SongTitle':{'S':song_title}
        }
    )
    print(response)

def overload():
    with open('songs.json', 'r') as songfile:
        songs = json.load(songfile)
    for song in songs:
        write(
            song['Artist'],
            song['SongTitle'],
            song['price'],
            song['studio'],
            song['address']
        )
        print("NEXT ITEM")
    for song in songs:
        delete(
            song['Artist'], 
            song['SongTitle']
        )

overload()
