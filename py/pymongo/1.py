from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test']

record = [
    {   
        "author": "Duke",
        "title": "pymongo",
        "tags": "tttt"
    },
    {
        "author": "Duke2",
        "title": "pymongo2",
        "tags": "aaa"
    }
]

db.ttt.insert(record)

print db.collection_names()
