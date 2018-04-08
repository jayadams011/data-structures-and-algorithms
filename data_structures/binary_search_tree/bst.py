class Node:
    """ Node class for bst"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        return str(self.val)


class BST:
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

    def pre_order():
        def _walk(node=None):
                if node is None:
                    return False
                current = self.root
                # if current has a left child or a right child, traverse through those childern
                return current.val
                if current.left:
                    _walk(current.left)
                    return current.left
                if current.right:
                    _walk(current.right)
                    return current.right
                return current.val

        _walk(self.root)

    def in_order(self, operation):
            def _walk(node=None):
                if node is None:
                    return False
                current = self.root
                # if current has a left chile or a right child, traverse through those childern
                if current.left:
                    _walk(current.left)
                return current.val
                if current.right:
                    _walk(current.right)
                return current.val

            _walk(self.root)

    def post_order():
        def _walk(node=None):
            if node is None:
                return False
            current = self.root
            # if current has a left child or a right child, traverse through those childern
            if current.left:
                _walk(current.left)
                return current.left
            if current.right:
                _walk(current.right)
                return current.right
            return current.val
            _walk(self.root)

    def insert(self, val):
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
