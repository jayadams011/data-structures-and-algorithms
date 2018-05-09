from .bst import BST


# def fizzbuzz(BST):
#     # import pdb; pdb.set_trace()
#     """ traveres and returns values in order"""
    # def _walk(node=None):
    #     # import pdb; pdb.set_trace()
    #     if node is None:
    #         return False
    #     current = node
    #     """ if current has a left child or a right child, traverse
    #     #  through those childern and returns the current value as it get
    #     # to the last left or right node """

    #     if current.left:
    #         _walk(current.left)
    #     x = current.val
    #     if x % 3 == 0 and x % 5 == 0:
    #         current.val == ('fizzbuzz')
    #     elif x % 5 == 0:
    #         current.val == ('buzz')
    #     elif x % 3 == 0:
    #         current.val == ('fizz')
    #     if current.right:
    #         _walk(current.right)

    # _walk(BST.root)

    # return BST

"""function takes a binary tree as an argument """


def fizzbuzztree(tree):
    def _walk(node=None):
        if node is None:
            return
        if node.left is not None:
            _walk(node.left)
        if node.val % 15 == 0:
            node.val = "fizzbuzz"
        elif node.val % 3 == 0:
            node.val = "fizz"
        elif node.val % 5 == 0:
            node.val = "buzz"
        if node.right is not None:
            _walk(node.right)
    if tree.root is None:
        return False
    else:
        _walk(tree.root)
    return tree
