class Node:
    """ Node class for bst, this allows BST to create an empty Node whne there
     is not a node. """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """ creates a representaton of the node to return"""
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        """ these return a string representtaion of Node value"""
        return str(self.val)


class BST:
    """ BST will traverse the tree suing functions to return the val of
    nodes at respective palces.  """
    def __init__(self, iter=[]):
        self.root = None
        if iter:
            for item in iter:
                self.insert(item)

        else:
            raise TypeError('must be iterable type')

    def __repr__(self):
        return '<BST Root {}>'.format(self.root.val)

    def __str__(self):
        return self.root.val

    def pre_order(self, operation):
        def _walk(node=None):
            """ if node is none - reurn false and make a new node and set
             that as root """
            if node is None:
                return False
            current = self.root
            """ if current has a left child or a right child, traverse
                through those childern """
            return current.val
        """ returns the current value of the node before anything happens. """
        if current.left:
            _walk(current.left)
            return current.left
        if current.right:
            _walk(current.right)
            return current.right
        operation(current.val)

        _walk(self.root)

    def in_order(self, operation):
        def _walk(node=None):
            if node is None:
                return False
            current = self.root
            """ if current has a left chile or a right child, traverse
            #  through those childern and returns the current value as it get 
            # to the last left or right node"""
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)
            operation(current.val)

        _walk(self.root)

    def post_order(self, operation):
        def _walk(node=None):
            if node is None:
                return False
            current = self.root
            """ if current has a left child or a right child,
            # traverse through those childern """
            if current.left:
                _walk(current.left)
                return current.left
            if current.right:
                _walk(current.right)
                return current.right
            operation(current.val)
            _walk(self.root)

    def insert(self, val):
        """ inserts a value in the correct placed based on val and the tree"""
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node
