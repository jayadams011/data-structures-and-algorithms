"""Tests."""

from .hash_table import HashTable


def test_hash_table_creation():
    """Test creating a Hash Table."""
    table = HashTable(50)
    assert len(table.buckets) == 50


def test_hash_key(empty_hash_table):
    """Test key is hashed."""
    assert empty_hash_table._hash_key('abc') == 294


def test_set(empty_hash_table):
    """Test set works."""
    empty_hash_table.set('abc', 'a')
    assert empty_hash_table.buckets[294].head.val['abc'] == 'a'


def test_get(empty_hash_table):
    """Test get works."""
    empty_hash_table.set('abc', 'a')
    assert empty_hash_table.get('abc') == 'a'
