

import binary_search


def test_array_if_empty(sorted_array, test_value, low, high):
    """
    Test check cases wheere array are empty
    """
    sorted_array = []
    test_value = 25
    assert binary_search.sub_binary_search(sorted_array, test_value, low,
                                           high) == -1


def test_val_in_array(sorted_array, test_value, low, high):
    """
    Test if current value is in the array
    """
    sorted_array = [10, 20, 30, 40, 50]
    test_value = 60
    assert binary_search.sub_binary_search(sorted_array, test_value,
                                           low, high) == -1
