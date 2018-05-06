"""Imports."""
import pytest
from hash_table import HashTable
from left_join import left_join


def test_for_empty_map(small_table, empty_hash_table):
    """Test for items in second hash map."""
    assert left_join(small_table, empty_hash_table) == [{'John': 1234},
     {'Jane': '123456'}, {'John': '123'}, {'Jane': 'abc'}]


def test_if_two_tables(small_table, large_table):
    """Test two filled tables."""
    assert left_join(small_table, large_table) == [['yellow', 'blue', 'green'], ['gray', 'brown', 'pink'], ['black', 'red', 'orange'], ['cyan', 'puce', 'white']]


def test_when_first_array_is_empty(small_table, empty_hash_table):
    """Test if first table hase no buckets."""
    assert left_join(empty_hash_table, small_table) == []
