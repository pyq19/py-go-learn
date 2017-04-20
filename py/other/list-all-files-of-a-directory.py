# `os.listdir()` will get you everything that's in a directory - files and directories

mypath = '.'

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for l in onlyfiles:
    print l

# append-vs-extend.py
# check-a-directory-exists-and-create-2.py
# check-a-directory-exists-and-create.py
# list-all-files-of-a-directory.py
# make-a-chain-of-function-decorators.py
# merge-two-dictionaries.py
# staticmethod-classmethod.py
# using-global-variables-in-other-function.py

# 2
print '*' * 20
import glob
print glob.glob('./*.py')
for g in glob.glob('./*.py'):
    print g

# ['./append-vs-extend.py', './check-a-directory-exists-and-create-2.py', './check-a-directory-exists-and-create.py', './list-all-files-of-a-directory.py', './make-a-chain-of-function-decorators.py', './merge-two-dictionaries.py', './staticmethod-classmethod.py', './using-global-variables-in-other-function.py']
# ./append-vs-extend.py
# ./check-a-directory-exists-and-create-2.py
# ./check-a-directory-exists-and-create.py
# ./list-all-files-of-a-directory.py
# ./make-a-chain-of-function-decorators.py
# ./merge-two-dictionaries.py
# ./staticmethod-classmethod.py
# ./using-global-variables-in-other-function.py

print '^' * 20
for i in glob.glob('*.py'):
    print i

# append-vs-extend.py
# check-a-directory-exists-and-create-2.py
# check-a-directory-exists-and-create.py
# list-all-files-of-a-directory.py
# make-a-chain-of-function-decorators.py
# merge-two-dictionaries.py
# staticmethod-classmethod.py
# using-global-variables-in-other-function.py
