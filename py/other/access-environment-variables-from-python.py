# http://stackoverflow.com/questions/4906977/access-environment-variables-from-python

import os
print os.environ['HOME'] # /Users/Mccree

print os.environ.get('HOME') # /Users/Mccree

print os.environ.get('NOT_EXIST') # None

print os.getenv('NOT_EXIST', 'lalala') # lalala

print 'HOME' in os.environ # True

# print os.environ

