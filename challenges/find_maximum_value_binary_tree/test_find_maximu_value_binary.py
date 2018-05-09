from .bst import BST
import pytest


def test_empty_bst_length(new_bst):
    """ test that root is non with empty tree """
    assert find_maximum_value(new_bst) is None


def test_data_bst_in_order_traverse(filled_bst):
    """ test for inorder taverse """
    assert find_maximum_value(filled_bst) == 20


def test_right_bst_breadth_first(right_bst):
    assert find_maximum_value(right_bst) == 10
