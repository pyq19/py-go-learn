import datetime
print datetime.datetime.now()
# 2017-04-04 16:43:25.393005

# >>> import datetime
# >>> datetime.datetime.now()
# datetime.datetime(2017, 4, 4, 16, 44, 3, 987677)


# >>> datetime.datetime.time(datetime.datetime.now())
# datetime.time(16, 44, 37, 946490)

print datetime.datetime.time(datetime.datetime.now())
# 16:45:11.658514


# >>> from time import gmtime, strftime
# >>> strftime("%Y-%m-%d %H:%M:%S", gmtime())
# '2017-04-04 08:46:51'


# >>> from datetime import datetime
# >>> str(datetime.now())
# '2017-04-04 16:47:53.593453'


# >>> datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# '2017-04-04 16:49:01'
