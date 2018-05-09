"""Test and test imports."""
from .quicksort import quicksort
import pytest


def test_empty_quick_sort():
    """Test empty quick sort."""
    assert quicksort([]) == ([])


def test_small_quick_sort():
    """Test small quick sort."""
    assert quicksort([2, 3, 1]) == ([1, 2, 3])


def test_large_quick_sort():
    """Test large quick sort."""
    assert quicksort([910, 78, 56, 34, 12]) == ([12, 34, 56, 78, 910])
