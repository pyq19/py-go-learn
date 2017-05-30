# http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory

# The __file__ is an attribute of the module object. You need run the code inside a Python file, not on the REPL

import os

print os.path.dirname(os.path.realpath(__file__))
# /Users/Mccree/p/py-go-learn/py/other

# to get the current working directory use
print os.getcwd()
# /Users/Mccree/p/py-go-learn/py/other

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))
