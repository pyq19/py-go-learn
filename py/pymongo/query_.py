#coding:utf8
# https://docs.mongodb.com/getting-started/python/query/

from pymongo import MongoClient

client = MongoClient()
db = client.test

# {  
#    "_id":ObjectId("591702280816b5054c90f157"),
#    "cuisine":"Italian",
#    "name":"Vella",
#    "restaurant_id":"41704620",
#    "grades":[  
#       {  
#          "date":         ISODate("2014-10-01T00:00:00         Z"),
#          "grade":"A",
#          "score":11
#       },
#       {  
#          "date":         ISODate("2014-01-16T00:00:00         Z"),
#          "grade":"B",
#          "score":17
#       }
#    ],
#    "address":{  
#       "building":"1480",
#       "street":"2 Avenue",
#       "zipcode":"10075",
#       "coord":[  
#          -73.9557413,
#          40.7720266
#       ]
#    },
#    "borough":"Manhattan"
# }
cursor = db.restaurants.find()

for document in cursor:
    print document
    print type(document)

# Query by a Top Level Field
cursor = db.restaurants.find({'borough': 'Manhattan'})

# Query by a Field in an Embedded Document
cursor = db.restaurants.find({'address.zipcode': '10075'})

# Query by a Field in an Array
cursor = db.restaurants.find({'grades.grade': 'B'})

# Less Than Operator ($lt)
# query for documents whose grades array contains an embedded document
# with a field score less than 10
cursor = db.restaurants.find({'grades.score': {'$lt': 10}})

# logical AND
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})

# logical OR
cursor = db.restaurants.find(
    {
        "$or": [
            {"cuisine": "Italian"},
            {"address.zipcode": "10075"}
        ]
    }
)

# Sort Query Results
print '=' * 20
# To specify an order for the result set, append the sort() method to the query. Pass to sort() method a document which contains the field(s) to sort by and the corresponding sort type, e.g. pymongo.ASCENDING for ascending and pymongo.DESCENDING for descending.
# 
# To sort by multiple keys, pass a list of keys and sort type pairs. For example, the following operation returns all documents in the restaurants collection, sorted first by the borough field in ascending order, and then, within each borough, by the "address.zipcode" field in ascending order:
import pymongo
cursor = db.restaurants.find().sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.ASCENDING)
])
for document in cursor:
    print(document)
