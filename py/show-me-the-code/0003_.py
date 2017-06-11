import redis
import random
import string

def gen_key(num):
    res = []
    for _ in xrange(num):
        res.append(''.join(random.choice(string.digits+string.letters) for _ in xrange(20)))
    return res
    

def save_to_redis(key_list):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for index, key in enumerate(key_list):
        r.set(index, key)


save_to_redis(gen_key(5))
