import copy, pprint

class Graph:
    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def addConnection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return '<Graph(%s) id(%s)>' % (self.name, id(self))

    def __deepcopy__(self, memo):
        print
        print repr(self)
        not_there = []
        existing = memo.get(self, not_there)
        if existing is not not_there:
            print ' Already copied to ->', repr(existing)
            return existing
        pprint.pprint(memo, indent=4, width=40)
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print ' Copying to ', repr(dup)
        memo[self] = dup
        for c in self.connections:
            dup.addConnection(copy.deepcopy(c, memo))
        return dup

root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.addConnection(a)
root.addConnection(b)

dup = copy.deepcopy(root)

# <Graph(root) id(4432113320)>
# {   }
#  Copying to  <Graph(root) id(4432220240)>
# 
# <Graph(a) id(4432113392)>
# {   <Graph(root) id(4432113320)>: <Graph(root) id(4432220240)>,
#     4432104304: 'root',
#     4432116264: ['root']}
#  Copying to  <Graph(a) id(4432220312)>
# 
# <Graph(root) id(4432113320)>
#  Already copied to -> <Graph(root) id(4432220240)>
# 
# <Graph(b) id(4432113464)>
# {   <Graph(root) id(4432113320)>: <Graph(root) id(4432220240)>,
#     <Graph(a) id(4432113392)>: <Graph(a) id(4432220312)>,
#     4431054328: 'a',
#     4432104304: 'root',
#     4432113320: <Graph(root) id(4432220240)>,
#     4432113392: <Graph(a) id(4432220312)>,
#     4432116264: [   'root',
#                     'a',
#                     <Graph(root) id(4432113320)>,
#                     <Graph(a) id(4432113392)>]}
#  Copying to  <Graph(b) id(4432220528)>
