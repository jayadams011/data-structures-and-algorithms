<<<<<<< HEAD
"""Test imports."""
from mergersort import mergersort
import pytest


def test_empty_merge_sort():
    """Test empty merge sort."""
    assert mergesort([]) == []
=======
>>>>>>> 6aa1735e4e4806585d18d3bc964bcfd818b1915c


def test_small_merge_sort():
    """Test merge sort."""
    assert mergesort([1234]) == [1234]


def test_large_merge_sort():
    """Test large merge sort."""
    assert mergesort([12, 34, 56, 78, 910, 876, 5432]) == [12, 34, 56, 78, 910,
                                                           876, 5432]
