"""Test and test imports."""
from .mergesort import mergesort
import pytest


def test_empty_merge_sort():
    """Test empty merge sort."""
    assert mergesort([]) == []


def test_small_merge_sort():
    """Test small merge sort."""
    assert mergesort([1, 2, 3]) == [1, 2, 3]


def test_large_merge_sort():
    """Test large merge sort."""
    assert mergesort([910, 78, 56, 34, 12]) == [12, 34, 56, 78, 910]
