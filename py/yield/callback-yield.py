def framework(logic):
    try:
        it = logic()
#        s = next(it)
        s = it.send(None)
        print 'logic -> ', s
        print 'do something ...'
        it.send('[async]' + s)
    except StopIteration:
        print 'stop iteration'
        
def logic():
    s = 'my logic()'
    r = yield s
    print 'logic recived ->', r

framework(logic)

# logic ->  my logic()
# do something ...
# logic recived -> [async]my logic()
# stop iteration

# logic ->  my logic()
# do something ...
# logic recived -> [async]my logic()
# stop iteration
