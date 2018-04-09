from bst import BST


def fizzbuzz(BST):
    # import pdb; pdb.set_trace()
    """ traveres and returns values in order"""
    def _walk(node=None):
        if node is None:
            return False
        current = node
        """ if current has a left child or a right child, traverse
        #  through those childern and returns the current value as it get
        # to the last left or right node """

        if current.left:
            _walk(current.left)
        operation(current.val)
        x = current.val
        if x % 3 == 0 and x % 5 == 0:
            current.val == ('fizzbuzz')
        elif x % 5 == 0:
            current.val == ('buzz')
        elif x % 3 == 0:
            current.val == ('fizz')
        if current.right:
            _walk(current.right)

    _walk(self.root)

    return BST
