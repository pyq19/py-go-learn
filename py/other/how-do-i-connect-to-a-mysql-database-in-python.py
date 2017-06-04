# coding:utf8
# https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python

import MySQLdb # pip install mysql-python

db = MySQLdb.connect(host='localhost',
                     user='root',
                     passwd='password',
                     db='test')

cur = db.cursor()

cur.execute('select * from t')

for row in cur.fetchall():
    print row[0]
    print row

db.close()
