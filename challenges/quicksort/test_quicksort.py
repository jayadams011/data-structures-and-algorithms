"""Test and test imports."""
from mergersort import mergersort
import pytest


def test_empty_merge_sort():
    """Test empty merge sort."""
    assert mergesort([]) == []


def test_small_merge_sort():
    """Test small merge sort."""
    assert mergesort([123]) == [123]


def test_large_merge_sort():
    """Test large merge sort."""
    assert mergesort([12, 34, 56, 78, 910]) == [910, 78, 56, 34, 12]