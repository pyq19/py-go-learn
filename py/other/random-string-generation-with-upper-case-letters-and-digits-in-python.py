# coding:utf8
# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

# 6U1S75
# 4Z4UKK
# U911K4


''.join(random.choice(string.ascii_uppercase + string.digits) for _ in xrange(N))

# 3.6 random.choices()
''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
