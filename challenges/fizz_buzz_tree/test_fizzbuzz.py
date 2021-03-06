from .bst import BST
from .fizzbuzztree import fizzbuzztree as fb
import pytest


@pytest.fixture
def new_bst():
    return BST()


@pytest.fixture
def filled_bst():
    return BST([4, 3, 2, 1, 8, 6, 12, 9])


def test_post_order_(new_bst):
    """empty bst"""
    assert fb(new_bst) is False


def test_data_bst_fizzbuzztree_in_order_traverse(filled_bst):
    filled_bst = fb(filled_bst)
    lst = []
    filled_bst.in_order(lst.append)
    assert lst == [1, 2, 'fizz', 4, 'fizz', 8,  'fizz', 'fizz']


def test_data_bst_fizzbuzztree_pre_order_traverse(filled_bst):
    filled_bst = fb(filled_bst)
    lst = []
    filled_bst.pre_order(lst.append)
    assert lst == [4, 'fizz', 2, 1, 8, 'fizz', 'fizz', 'fizz']
