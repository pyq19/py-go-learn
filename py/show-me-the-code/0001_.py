# coding:utf8

import random
import string

def gen_str(num):
    res = []
    for _ in xrange(num):
        res.append((''.join(random.choice(string.letters+string.digits) for _ in xrange(20))))
    return res
    
print gen_str(10)
