# coding:utf8

import random
import string
import MySQLdb

def gen_str(num):
    res = []
    for _ in xrange(num):
        res.append((''.join(random.choice(string.letters+string.digits) for _ in xrange(20))))
    return res


def save_to_mysql(key_list):
    db = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='forever367',
        db='test'
    )
    cursor = db.cursor()
    cursor.execute('drop table if exists ukey')
    sql = '''create table ukey (
            key_value char(40) not null
            )'''
    cursor.execute(sql)

    try:
        for key in key_list:
            cursor.execute('insert into ukey values("%s")' % key)
        db.commit()
    except:
        db.rollback()
    db.close()


if __name__ == '__main__':
    key_list = gen_str(20)
    save_to_mysql(key_list)
