#coding:utf8
# although implementing __setattr__ is not that common of a practice,
# we thought we'd include a discussion of it for the sake of completeness.
# Basically, __setattr__ allows you to override Python's default mechanism for
# member assignment(分配，任务，作业，功课).

# __setattr__ is not symmetrical(对称的) to __getattr__
# in particular(特别的，详细的), all attribute assignments(分配) go
# through __setattr__, even for variables that are present in the __dict__ magic
# variable. For this reason, we don't recommend implementing __setattr__.

class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print 'set %s to %s' % (name, repr(value))

        if name in ('a', 'b'):
            object.__setattr__(self, name, value)

t = Test()
t.c = 'z'
setattr(t, 'd', '888')

# set a to 'a'
# set b to 'b'
# set c to 'z'
# set d to '888'
