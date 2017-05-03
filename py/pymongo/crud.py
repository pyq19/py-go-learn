from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017')

db = client['test']

posts = db.posts

post = {
    'author': 'Mike',
    'test': 'My first blog post!',
    'tags': ['mongodb', 'python', 'pymongo'],
    'count': 1,
    'date': datetime.datetime.utcnow()
}

# Insert
post_id = posts.insert(post)
print 'post_id ->', post_id

# Buld Insert
new_posts = [
    
]

# Find
print 'posts.find_one() -->', posts.find_one()
print "posts.find_one({'author': 'Mike'})--->", posts.find_one({'author': 'Mike'})
print "posts.find_one({'author': 'Eliot'})--->", posts.find_one({'author': 'Eliot'})
print "posts.find_one({'_id': post_id})--->", posts.find_one({'_id': post_id})
print "posts.find_one({'_id': str(post_id)})----->", posts.find_one({'_id': str(post_id)}) # no result
#print posts.find_one({'_id': ObjectId(str(post_id))}) # from bson.objectid import ObjectId

for post in posts.find({'title': 'MongoDB is fun'}):
    print "post----->", post

# Update
print posts.update({'author': 'Mike'}, {'$inc': {'count': 1}}, multi=True)
for doc in posts.find({'author': 'Mike'}):
    posts.find({'title': 'MongoDB is fun'}).count()
    print "doc----->", doc
# update_one
# >>> col.update_one({"name":"John"}, {"$set":{"name":"Joseph"}})
# <pymongo.results.UpdateResult object at 0x7f8fbe7fb910>
#
# # update_many
# >>> col.update_many({"name":"John"}, {"$set":{"name":"Joseph"}})
# <pymongo.results.UpdateResult object at 0x7f8fbe7fb7d0>
#
# # update
# >>> col.update({"name":"John"}, {"$set":{"name":"Jeorge"}})
# {'updatedExisting': False, u'nModified': 0, u'ok': 1, u'n': 0}
#
# #replace_one
# >>> col.replace_one({"name":"John"}, {"name":"Jeorge"})
# <pymongo.results.UpdateResult object at 0x7f8fbe7fb910>

# FindAndModify
print "posts.find_and_modify({'author': 'Mike'}, {'$push': {'tags': 'modify'}}, new=True)----->", posts.find_and_modify({'author': 'Mike'}, {'$push': {'tags': 'modify'}}, new=True)

# Remove
posts.remove({'author': 'Mike'})

# Counting
print "posts.count()----->", posts.count()
print "posts.find({'title': 'MongoDB is fun'}).count()----->", posts.find({'title': 'MongoDB is fun'}).count()
