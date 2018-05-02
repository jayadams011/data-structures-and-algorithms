"""Imports."""
from bst import BST
import pytest
from tree_intersection import tree_intersection


def test_empty_tree(empty_bst, small_bst):
    """Tests for empty tree."""
    assert tree_intersection(empty_bst, small_bst) is False


def test_small_bst(small_bst, big_bst):
    """Test correct answer."""
    assert tree_intersection(small_bst, big_bst) == [2, 4, 5, 6, 7]
