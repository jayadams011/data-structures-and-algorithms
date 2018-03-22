

import shift-array.pytest

import pytest


def test_shift_array_if_len_odd():
    """
    test for if  number of elements is odd
    """
    old_array = [0, 0, 0]
    value = 1
    shift-array()
    assert old_array[2] == 1


def test_shift_array_if_len_even():
    """
    test for if number of elements is even
    """
    old_array = [0, 0, 0, 0]
    value = 1
    shift-array()
    assert old_array[2] == 1


def test_shift_array_if_is_empty():
    """
    test for if array is empty
    """
    old_array = []
    value = 1
    assert old_array[0] == 1
