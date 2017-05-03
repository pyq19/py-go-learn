from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test']

db.posts.drop()

post = {
    "author": "duke",
    "title": "pymon",
    "tag": "tag.."
}

posts = db.posts
#post_id = posts.insert(post)
print posts.insert(post)

