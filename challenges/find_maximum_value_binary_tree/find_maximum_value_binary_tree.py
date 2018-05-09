def find_maximum_value(tree):
        max_val = root.val
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
            if current.val >= max_val
            max_val == current.val

            if current.right:
                _walk(current.right)

        _walk(self.root)
        return max-val
