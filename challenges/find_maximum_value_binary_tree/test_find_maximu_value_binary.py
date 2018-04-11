from .bst import BST


def test_empty_bst_length(new_bst):
    """ test that root is non with empty tree """
    assert new_bst.root is None


def test_data_bst_in_order_traverse(filled_bst):
    """ test for inorder taverse """
    lst = []
    filled_bst.in_order(lst.append)
    assert lst == [1, 2, 3, 4, 6, 8, 9, 12]









