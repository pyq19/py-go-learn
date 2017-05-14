#coding:utf8
# https://docs.mongodb.com/getting-started/python/update/

from pymongo import MongoClient
client = MongoClient()
db = client.test

# {  
#    "_id":ObjectId("591702280816b5054c90f157"),
#    "cuisine":"American (New)",
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
#       "street":"East 31st Street",
#       "zipcode":"10075",
#       "coord":[  
#          -73.9557413,
#          40.7720266
#       ]
#    },
#    "borough":"Manhattan",
#    "lastModified":   ISODate("2017-05-13T16:52:18.274   Z")
# }

result = db.restaurants.update_one(
    {"name": "Vella"},
    {
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)
print result.matched_count # 1

print 'Update an Embedded Field'
result = db.restaurants.update_one(
    {'restaurant_id': '41704620'},
    {'$set': {'address.street': 'East 31st Street'}}
)
print result.matched_count

# Update Multiple Documents
# 
# The update_one() method updates a single document. To update multiple documents, use the update_many() method. The following operation updates all documents that have address.zipcode field equal to "10016" and cuisine field equal to "Other", setting the cuisine field to "Category To Be Determined" and the lastModified field to the current date.
# 
# result = db.restaurants.update_many(
#     {"address.zipcode": "10016", "cuisine": "Other"},
#     {
#         "$set": {"cuisine": "Category To Be Determined"},
#         "$currentDate": {"lastModified": True}
#     }
# )

print 'Replace a Document'
result = db.restaurants.replace_one(
    {"restaurant_id": "41704620"},
    {
        "name": "Vella 2",
        "address": {
            "coord": [-73.9557413, 40.7720266],
            "building": "1480",
            "street": "2 Avenue",
            "zipcode": "10075"
        }
    }
)
print result.matched_count # 1
print result.modified_count # 1
# {  
#    "_id":ObjectId("591702280816b5054c90f157"),
#    "name":"Vella 2",
#    "address":{  
#       "building":"1480",
#       "street":"2 Avenue",
#       "zipcode":"10075",
#       "coord":[  
#          -73.9557413,
#          40.7720266
#       ]
#    }
# }
