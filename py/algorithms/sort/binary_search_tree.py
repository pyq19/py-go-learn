#coding:utf8

class Node(object):
    def __init__(self, payload): # payload 有效负荷，载重
        self.payload = payload
        self.left = self.right = 0
        # this concludes the 'how to represent' asked in the question.
        # Once you represent a BST tree like this, you can of course add a variety of methods to modify it,
        # 'walk' over it, and so forth, such as:
    
    def insert(self, othernode):
        ' insert node `othernode` under Node `self`.'
        if self.payload <= othernode.payload:
            if self.left: self.left.insert(othernode)
            else: self.left = othernode
        else:
            if self.right: self.right.insert(othernode)
            else: self.right = othernode
        
    def inorderwalk(self):
        ' yield this Node and all under it in increasing-payload order.'
        if self.left:
            for x in self.left.inorderwalk(): yield x
        yield self
        if self.right:
            for x in self.right.inorderwalk(): yield x
    
    def sillywalk(self):
        'tiny, silly subset of `inorderwail` functionality as requested'
        if self.left:
            self.left.sillywalk()
        print(self.payload)
        if self.right:
            self.right.sillywalk()
        
