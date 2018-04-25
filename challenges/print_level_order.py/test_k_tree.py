import pytest


def test_pre_order_k_tree(filled_tree):
    lst = []
    filled_tree.pre_order(lst.append)
    assert lst == []
