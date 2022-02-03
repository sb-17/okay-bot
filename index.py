import collections
import discord
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

def get_database():
    from pymongo import MongoClient

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.getenv("MONGOURI")
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['okaycounter']

db = get_database()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.channel.id == 938367285834420245:
        if message.content == '.' or message.content.lower() == 'okay' or message.content.lower() == 'ok' or message.content.lower() == 'k' or message.content.lower() == 'okej':
            collection = db["counter"]
            num = collection.find_one({ '_id': ObjectId("61fa5e650bee30fe96c86643") })
            myquery = { '_id': ObjectId("61fa5e650bee30fe96c86643") }
            newvalues = { '$set': { 'count': str(int(num["count"]) + 1) } }
            collection.update_one(myquery, newvalues)
            await message.reply("Okay counter: " + str(int(num["count"]) + 1))

client.run(os.getenv("TOKEN"))