# coding:utf8
# https://github.com/Show-Me-the-Code/python/blob/master/renzongxian/0001/0001.py


import uuid


def gen_key():
    key_list = []
    for i in xrange(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-', ''))
    return key_list


if __name__ == '__main__':
    print gen_key()
