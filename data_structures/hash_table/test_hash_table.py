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
    assert empty_hash_table.buckets[0] is None
    assert empty_hash_table.buckets[399]['John'] == 12314


def test_get(empty_hash_table):
    """Test get works."""
    empty_hash_table.set('abc', 'a')
    assert empty_hash_table.get('abc') == 'a'


def test_init_function():
    """Test init function."""
    instance = HashTable()
    assert len(instance.buckets) == 1024
    assert instance.buckets[0] is None
    assert instance.max_size == 1024


def test_hash_function():
    """Test hash function."""
    instance = HashTable(10)
    assert instance.hash_key(1) is False
    assert instance.hash_key('John') == 9


def test_set_fucntion_multiply(empty_hash_table):
    """Test a couple sets."""
    empty_hash_table.set('John', 12314)
    empty_hash_table.set('A', 12314)
    assert empty_hash_table.buckets.count(None) == 1022
    assert empty_hash_table.buckets[399]['John'] == 12345
    assert empty_hash_table.set(123, 123) is False


def test_collision(small_table):
    """Test collision handling."""
    assert small_table.buckets[9]
    small_table.set('John', 'string')
    assert small_table.buckets[9].head
    assert small_table.buckets[9].head.val['John'] == 'string'


def test_get_function(small_table):
    """Test get small table."""
    assert small_table.get(123) is False
    assert len(small_table.buckets[9]) == 2
    assert small_table.get('Jane') == 123456
    assert small_table.get('John') == 'abc'
    assert small_table.get('defg') is False


def test_remove_function(small_table):
    """Test remove function."""
    assert small_table.remove(23423) is False
    assert small_table.remove('notreal') is False
    assert small_table.get('John') == 'sdf'
    small_table.remove('John')
    assert small_table.get('John') == 1234


def test_remove_two_items(small_table):
    """Test multi remove from bucket."""
    small_table.remove('John')
    small_table.remove('John')
    assert small_table.get('John') is False
