"""Imports."""
import pytest
from hash_table import HashTable
from left_join import left_join


@pytest.fixture
def empty_hash_table():
    """Make empty table."""
    return HashTable()


@pytest.fixture
def table_one():
    """Small table."""
    small_table = HashTable(100)
    small_table.set('one', 'blue')
    small_table.set('two', 'green')
    small_table.set('three', 'yellow')
    small_table.set('four', 'red')
    return small_table


@pytest.fixture
def table_two():
    """Big table."""
    big_table = HashTable(100)
    big_table.set('ten', 'black')
    big_table.set('twenty', 'white')
    big_table.set('thirty', 'purple')
    big_table.set('forty', 'cyan')
    big_table.set('fifty', 'gray')
    return big_table


# @pytest.fixture
# def empty_bst():
#     """Empty bst."""
#     return BST()


# @pytest.fixture
# def small_bst():
#     """Sm bst."""
#     return BST([4, 3, 3.5, 2, 5, 6, 7])


# @pytest.fixture
# def big_bst():
#     """Big bst."""
#     return BST([4, 2, 2.5, -1, 5, 6, 7])


# @pytest.fixture
# def ss_bst():
#     """SS bst."""
#     return BST([1, 2, 6, 0, 7, 4, 2])
