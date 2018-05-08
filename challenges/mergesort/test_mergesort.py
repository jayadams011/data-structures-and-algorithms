"""Test imports."""
from mergersort import mergersort
import pytest


def test_empty_merge_sort():
    """Test empty merge sort."""
    assert mergesort([]) == []


def test_small_merge_sort():
    """Test merge sort."""
    assert mergesort([1234]) == [1234]


def test_large_merge_sort():
    """Test large merge sort."""
    assert mergesort([12, 34, 56, 78, 910, 876, 5432]) == [12, 34, 56, 78, 910,
                                                           876, 5432]
