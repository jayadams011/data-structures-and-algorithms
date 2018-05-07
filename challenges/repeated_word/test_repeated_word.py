"""Tests for repeated words."""

from .repeated_words import repeated_words
from .hash_table import HashTable
import pytest


@pytest.fixture
def empty_hash_table():
    """Empty hash table."""
    return HashTable()


@pytest.fixture
def basic_hash_table():
    """Not empty hash table."""
    return HashTable(1)


def test_basic_repeat():
    """Test with basic string."""
    assert repeated_words('word word') == 'word'


def test_empty_string():
    """Test empty string."""
    assert repeated_words('') is None


def test_complex_string():
    """Test a complex string."""
    complex_string = 'I hope this works and makes Marco happy that it works'
    assert repeated_words(complex_string) == 'works'
