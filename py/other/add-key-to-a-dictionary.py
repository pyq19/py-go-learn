d = {'key': 'value'}
print d
# {'key': 'value'}

d['mynewkey'] = 'mynewvalue'
print d
# {'mynewkey': 'mynewvalue', 'key': 'value'}



x = {1: 2, 3: 4}
print x
# {1: 2, 3: 4}

x.update({5: 6})
print x
# {1: 2, 3: 4, 5: 6}
