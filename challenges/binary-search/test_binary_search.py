

import binary_search


def test_sorted_array_is_empty():
    """
    test if sorted array is empty
    """
    sorted_array = []
    test_value = 2
    assert sorted_array(sorted_array, test_value)


def test_newtest_value_in_sorted_array():
    """
    test if test_value in sorted_array
    """
    sorted_array = [10, 20, 30, 40, 50]
    test_value = 90
    assert binary_search(sorted_array, test_value) == -1


def test_big_test_value_in_sorted_array():
    """
    test if test_value in very big sorted_array
    """
    test_value = 1000
    assert binary_search(sorted_array(range(10000)), test_value) == -1


def test_test_array():
    """
    test output form test_array
    """
    sorted_array = [10, 20, 30]
    test_value = 20
    assert binary_search(sorted_array, test_value) == 1
