"""Imports."""
from bst import BST
import pytest
from tree_intersection import tree_intersection


@pytest.fixture
def empty_bst():
    """Empty bst."""
    return BST()


@pytest.fixture
def small_bst():
    """Sm bst."""
    return BST([4, 3, 3.5, 2, 5, 6, 7])


@pytest.fixture
def big_bst():
    """Big bst."""
    return BST([4, 2, 2.5, -1, 5, 6, 7])


@pytest.fixture
def ss_bst():
    """SS bst."""
    return BST([1, 2, 6, 0, 7, 4, 2])
