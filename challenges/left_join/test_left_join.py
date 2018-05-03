"""Imports."""
import pytest
from hash_table import HashTable
from left_join import left_join


def test_for_empty_map(table_one, empty_hash_table):
    """Test for items in second hash map."""
    assert left_join(table_one, empty_hash_table) == [{'one': 'blue'},
                                                      {'two': 'green'},
                                                      {'three': 'yellow'},
                                                      {'four': 'red'}]


# def test_empty_tree(empty_bst, small_bst):
#     """Tests for empty tree."""
#     assert tree_intersection(empty_bst, small_bst) is False


# def test_small_bst(small_bst, big_bst):
#     """Test correct answer."""
#     assert tree_intersection(small_bst, big_bst) == [2, 4, 5, 6, 7]
