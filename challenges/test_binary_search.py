

import binary_search

import pytest


def test_sorted_array_is_empty():
    """
    test if sorted array is empty
    """
    sorted_array = []
    test_value = 2
    assert binary_search(sorted_array, test_value)


def test_test_value_in_sorted_array():
    """
    test if test_value in sorted_array
    """
    sorted_array = [10, 20, 30, 40, 50]
    test_value = 90
    assert binary_search(sorted_array, test_value) == -1


def test_test_array():
    """
    test output form test_array
    """
    sorted_array = [10, 20, 30]
    test_value = 20
    assert binary_search(sorted_array, test_value) == 1
