def test_empty_bst_length(new_bst):
    """ test that root is non with empty tree """
    assert new_bst.root is None


def test_empty_bst_insert(new_bst):
    """ test that not empty after insert """
    new_bst.insert(1)
    assert new_bst.root is not None


def test_data_bst_insert_negative_left(filled_bst):
    """ test if a neg val can be inserted """
    filled_bst.insert(-1)
    assert filled_bst.root.left.left.left.left.val == -1


def test_data_bst_in_order_traverse(filled_bst):
    """ test for inorder taverse """
    lst = []
    filled_bst.in_order(lst.append)
    assert lst == [1, 2, 3, 4, 6, 8, 9, 12]


def test_data_bst_pre_order_traverse(filled_bst):
    """ test for pre order traverse """
    lst = []
    filled_bst.pre_order(lst.append)
    assert lst == [4, 3, 2, 1, 8, 6, 12, 9]


def test_data_bst_post_order_traverse(filled_bst):
    """ test for post order traveres """
    lst = []
    filled_bst.post_order(lst.append)
    assert lst == [1, 2, 3, 6, 9, 12, 8, 4]


def test_empty_bst_post_order(new_bst):
    """ test if post oreder catches insert """
    new_bst.insert(1)
    assert new_bst.post_order is not None


# def test_repr(filled_bst):
""" testing for repr return """
#     assert filled_bst.__repr__() == '<Node Val: {}'.format(self.val)


# def test_str(filled_bst):
""" Testing for str return """
#     assert filled_bst.__str__() == [4, 3, 2, 1, 8, 6, 12, 9]
