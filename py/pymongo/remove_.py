#coding:utf8
# https://docs.mongodb.com/getting-started/python/remove/

from pymongo import MongoClient
client = MongoClient()
db = client.test

result = db.restaurants.delete_many({'borough': 'Manhattan'})
print result.deleted_count # 1

print 'Remove All Documents'
result = db.restaurants.delete_many({})

print 'Drop a Collection'
db.restaurants.drop()
