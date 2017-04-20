# make two decorators in python that would do the following

# @makebold
# @makeitalic
# def say():
#     return 'hello'
# 
# # which should return
# '<b><i>hello</i></b>'


def makebold(fn):
    def wrapped():
        return '<b>' + fn() + '</b>'
    return wrapped

def makeitalic(fn):
    def wrapped():
        return '<i>' + fn() + '</i>'
    return wrapped

@makebold
@makeitalic
def say():
    return 'hello'

print(say())
# which should return
# '<b><i>hello</i></b>'


