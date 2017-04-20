a = '545.2222'

print 'a ->', a
# a -> 545.2222

print 'float(a) -> ', float(a)
# float(a) ->  545.2222

print 'int(float(a)) ->', int(float(a))
# int(float(a)) -> 545


def num(string_num):
    try:
        return int(string_num)
    except ValueError:
        return float(string_num)

print 'num(a) ->', num(a) # num(a) -> 545.2222
print 'num(num(a)) ->', num(num(a)) # num(num(a)) -> 545
