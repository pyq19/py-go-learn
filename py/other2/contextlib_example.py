#coding:utf8

from contextlib import contextmanager


@contextmanager
def closing(o):
    print '__enter__'
    yield o
    print '__exit__'
    o.close()

with closing(open('README.md', 'r')) as f:
    print f.readline()

# __enter__
# ~/p/py-go-learn/py/other2(master ✗) vi contextlib_example.py
# 
# __exit__
