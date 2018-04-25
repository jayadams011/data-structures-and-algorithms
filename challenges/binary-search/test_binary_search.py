
import pytest
from binary_search import binary_search

TEST_ARRAY = [1, 2, 3, 4, 5, 6] 


def test_array_if_empty():
    """Test check cases where array is empty."""
    arr = []
    x = 25
    assert binary_search(arr, x) == -1


def test_x_not_int():
    """Test when x is not an integer"""
    x = 'hey'
    with pytest.raises(TypeError):
        binary_search(TEST_ARRAY, x)
