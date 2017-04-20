import hashlib

md5 = hashlib.md5()
password = 'asdasdasd'
md5.update(password.encode('utf-8'))
print(md5.hexdigest())


sha1 = hashlib.sha1()
sha1.update(password.encode('utf-8'))
print(sha1.hexdigest())

