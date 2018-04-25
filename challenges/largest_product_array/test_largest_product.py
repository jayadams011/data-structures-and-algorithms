from largest_product.py import largest_product
import pytest


def test_product_returns():
   """test if return is a single product """
    assert largest_product.largest([[2, 2]]) is 4


def test_returns_largest():
    """ test if return is the largest of longer array """
    assert largest_product.largest([[1, 3], [6, 10], [4, 5]]) is 60


def test_empty_list():
    """ test if returns msg if empty list """
    assert largest_product.largest([]) == 'empty arr used'


def test_check_if_syb_has_only_1_el():
    """test for one value"""
    arr = [3]
    val = 0
    assert largest_product.node_inside(arr, val) == 3
