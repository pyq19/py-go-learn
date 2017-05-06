#coding:utf8

import random
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017/')
#client.drop_database('test')           # 删除test 数据库
db = client.test                        # 使用test数据库
ttt = db.ttt                            # 使用ttt 这个collection

# 插入单条记录
rs = ttt.insert_one({'a': 1, 'b': 2})
object_id = rs.inserted_id
print object_id                         # 590c45c10816b525cd809c45

# 插入多条记录
rs = ttt.insert_many(
    [
        {'a': random.randint(1, 10), 'b': 10} for _ in range(10)
    ]
)
print rs.inserted_ids                   # 打印插入的对象id 列表

# 查询单条（符合的第一条）记录
print ttt.find_one({'a': 1, 'b': 2})

# 集合当前全部文档数
print ttt.count()

cursor = ttt.find({'a': {'$lte': 1}})   # 查询结果是一个游标
print cursor.count()                    # 符合查询的文档数

for r in cursor:
    print r, r['b']                     # 打印符合查询的文档内容，以及其中b 键的值
# 这个for 循环只能执行一次，如果想再获得查询结果，需要重新find 或者使用list(cursor) 把结果存起来

# 对查询结果排序
print list(ttt.find({'a': {'$lte': 1}}).sort([('b', -1)]))
# -1 也可以表示为pymongo.DESCENGINE

# 对查询结果可以限制返回文档数，控制跳过的结果数
print ttt.find({'b': {'$gt': 1}}).limit(1).skip(1).next()   # next 相当于find_one

# 找到后更新
# 第一个参数是过滤条件，第二个参数是要更新的操作（设置b为3，a自增长1）
# upsert 为True 表示找不到会创建一条记录，可以理解为get_or_create
rs = ttt.find_one_and_update(
    {'a': 1, 'b': 2},
    {'$set': {'b': 3}, '$inc': {'a': 1}},
    upsert=False
)
print rs    # 返回更新前的文档
# 同样的还有find_one_and_replace 和find_one_and_delete
print list(ttt.find({'a': 2, 'b': 2}))  # 上述文档已经更新为这个文档
ttt.find_one_and_update(
    {'a': 1, 'b': 2},
    {'$set': {'b': 3}, '$inc': {'a': 1}},
    upsert=True
)       # 虽然没有符合{'a': 1, 'b': 2}的记录但是会新建一个
print ttt.find({'a': 2, 'b': 3}).count()# 发现现在有两条文档记录了

print '*' * 20

# 删除单个文档
ttt.delete_one({'a': 2, 'b': 3})

# 一次性删除多个文档

rs = ttt.delete_many({'a': 2, 'b': 3})
# 如果没有符合的条目也不会提示，但是可以通过rs.delete_count 获得删除的数量
print rs.deleted_count
