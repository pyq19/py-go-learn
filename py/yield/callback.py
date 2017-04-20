def framework(logic, callback):
    s = logic()
    print 'logic -> ', s
    print 'do something.........'
    callback('(in framework) callback() async -> ' + s)

def logic():
    return 'in logic(), this is s'

def callback(s):
    print 'this is callback(s), s is -> ', s

framework(logic, callback)

# logic ->  in logic(), this is s
# do something.........
# this is callback(s), s is ->  (in framework) callback() async -> in logic(), this is s
