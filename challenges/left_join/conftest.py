"""Imports."""
import pytest
from hash_table import HashTable
from left_join import left_join


@pytest.fixture
def empty_hash_table():
    """Make empty table."""
    return HashTable()


@pytest.fixture
def small_table():
    """Small table."""
    small_table = HashTable(10)
    small_table.set('John', 1234)
    small_table.set('Jane', 123456)
    small_table.set('John', '123')
    small_table.set('Jane', 'abc')
    return small_table


@pytest.fixture
def large_table():
    """Large table."""
    large_table = HashTable()
    large_table.set('John', 1234)
    large_table.set('Jane', 123456)
    large_table.set('John', '123')
    large_table.set('Jim', 'abc')
    large_table.set('Jane', 123456)
    large_table.set('Jane', '123')
    large_table.set('Jane', 'abc')
    return large_table



