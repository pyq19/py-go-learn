# http://stackoverflow.com/questions/466345/converting-string-into-datetime

# Jun 1 2005    1:33PM
# Aug 28 1999   12:00AM

from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005 1:33PM', '%b %d %Y %I:%M%p')
print datetime_object
print type(datetime_object)
# 2005-06-01 13:33:00
# <type 'datetime.datetime'>

# http://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date


