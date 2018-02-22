import boto3
import json

dynamodb = boto3.client('dynamodb')

def write(artist, song_title, price, studio, address):
    response = dynamodb.put_item(
        TableName='MusicTest', 
        Item={
            'Artist':{'S':artist},
            'SongTitle':{'S':song_title},
            'price':{'S': price},
            'studio':{'S': studio},
            'address':{'S': address}
        }
    )
    print(response)

def upload():
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

# Song we want:
# {
#     "Artist": "Anthony Haslett",
#     "SongTitle": "December Lavender",
#     "price": "$1.05",
#     "studio": "PHOTOBIN",
#     "address": "886 Locust Avenue, Suitland, Vermont, 8689"
# },

def get_item(artist, song_title):
    dynamodb.get_item(
        TableName='MusicTest', 
        Key={
            'Artist':{'S':artist},
            'SongTitle':{'S':song_title}
        },
        ReturnConsumedCapacity='TOTAL'
    )

get_item("Anthony Haslett", "December Lavender")

def query():

def scan():
