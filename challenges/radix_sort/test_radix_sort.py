"""Test and test imports."""
from .radix_sort import radix_sort
import pytest


def test_empty_radix_sort():
    """Test empty radix sort."""
    assert radix_sort([]) == []


def test_small_radix_sort():
    """Test small radix sort."""
    assert radix_sort([1, 2, 3]) == [1, 2, 3]


def test_large_radix_sort():
    """Test large radix sort."""
    assert radix_sort([910, 78, 56, 34, 12]) == [12, 34, 56, 78, 910]