#coding:utf8
# https://gist.github.com/pingwping/92219a8a1e9d44e1dd8a

from mongoengine import *

# {
#     "_id" : ObjectId("59157c750816b51d5a5c9fe6"), 
#     "title": "Quora rocks", 
#     "author": "ross", 
#     "tags": [
#         "toturial", 
#         "how-to"
#     ], 
#     "comments": [
#         {
#             "content": "Great post!!", 
#             "name": "john"
#         }
#     ]
# }

connect('test5')

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = StringField(required=True)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))


# create a post
post = Post(title='Quora rocks', author='ross', tags=['toturial', 'how-to'])
post.save()
# find a post
# post = Post.objects.get(title='Quora rocks').first() # error !!
post = Post.objects(title='Quora rocks').first() # 只选第一个 !!

# create a new comment
comment = Comment(content='Great post!!', name='john')
# add to comments list and save
post.comments.append(comment)
post.save()


# to editing existing comments you can use atomic updates[1] or 
# simply change the comment and call post.save()
# (this will also do an atomic update).

# update
post = Post.objects(title='Quora rocks').first()
post.comments[0].name = 'Mccree'
post.save()

# or update with a set operation        # 注意comments
post = Post.objects(title='Quora rocks', comments__name='john').update(set__comments__S__name='Mccree')
# 不需要save

# {
#     "_id" : ObjectId("59157c750816b51d5a5c9fe6"), 
#     "title": "Quora rocks", 
#     "author": "ross", 
#     "tags": [
#         "toturial", 
#         "how-to"
#     ], 
#     "comments": [
#         {
#             "content": "Great post!!", 
#             "name": "Mccree"
#         }
#     ]
# }

