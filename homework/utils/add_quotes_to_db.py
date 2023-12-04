import json
from bson import objectid

from pymongo import MongoClient

client = MongoClient("mongodb://localhost")

db = client.hw

with open("../quotes/quotes.json", "r", encoding="utf-8") as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': objectid.ObjectId(author['_id'])
        })
