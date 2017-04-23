'''
    binary search tree
    ------------------
    the binary search tree represents an ordered symbol table of generic
    key-value pairs. keys must be comparable. does not permit duplicate keys.
    when assocating a value with a key already present in the BST, the previous
    value is replaced by the new one. this implementation is for an unbalanced BST.
'''

class Node(object):
    '''
    Implementation of a Node in Binary Search Tree.
    '''
    def __init__(self, key=None, val=None, size_of_subtree=1):
        self.key = key
        self.val = val
        self.size_of_subtree = size_of_subtree
        self.left = None
        self.right = None

class BinarySearchTree(object):
    '''
    Implementation of a Binary Search Tree
    '''

    def __init__(self):
        self.root = None

    def _size(self, node):
        if node is None:
            return 0
        else:
            return node.size_of_subtree

    def size(self):
        '''
        Return the number of nodes in the BST

        Worst Case Complexity: O(1)

        Balanced Tree Complexity: O(1)
        '''
        return self._size(self.root)

    def is_empty(self):
        '''
        Returns True if the BST is empty, False otherwise

        Worst Case Complexity: O(1)

        Balanced Tree Complexity: O(1)
        '''
        return self.size() == 0

    def _get(self, key, node):
        if node is None:
            return None
    
        if key < node.key:
            return self._get(key, node.left)
        elif key > node.key:
            return self._get(key, node.right)
        else:
            return node.val
    
    def get(self, key):
        '''
        Return the value paired with `key`

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        '''
        return self._get(key, self.root)
    
    def contains(self, key):
        '''
        Returns True if the BST contains 'key', False otherwise

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        '''
        return self.get(key) is not None

    def _put(self, key, val, node):
        # If we hit the end of a branch, create a new node
        if node is None:
            return Node(key, val)
        
        # Follow left branch
        if key < node.key:
            node.left = self._put(key, val, node.left)
        # Follow right branch
        elif key > node.key:
            node.right = self._put(key, val, node.right)
        # Overwrite value
        else:
            node.val = val

        node.size_of_subtree = self._size(node.left) + self._size(node.right) + 1
        return node

    def put(self, key, val):
        '''
        Add a new key-value pair.

        Worst Case Complexity: O(lg N)

        Balanced Tree Complexity: O(lg N)
        '''
        self.root = self._put(key, val, self.root)

    def _min_node(self):
        '''
        Return the node with the minimum key in the BST
        '''
        min_node = self.root
        # Return none if empty BST
        if min_node is None:
            return None

        while min_node.left is not None:
            min_node = min_node.left

        return min_node

    def min_key(self):
        '''
        Return the minimum key in the BST

        Worst Case Complexity: O(N)

        Balanced Tree Complexity: O(lg N)
        '''
        min_node = self._min_node()
        if min_node is None:
            return None
        else:
            return min_node.key

    def _max_node(self):
        pass # !!!
