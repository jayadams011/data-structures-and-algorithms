def sub_binary_search(sorted_array, test_value, low, high):
    """ run through sorted_array and look for test_value.
    if test_value is in sorted_array, return index for test_value
    in sorted_array. If test_value is not in sorted_array, return
    -1 """
    if low > high:
        False
    else:
        mid = (low+high)//2
        if test_value == sorted_array[mid]:
            print(mid)
            return mid
        elif test_value < sorted_array[mid]:
            return sub_binary_search(sorted_array, test_value, low, mid-1)
        else:
            return sub_binary_search(sorted_array, test_value, mid+1, high)


def binary_search1(sorted_array, test_value, low, high):

    if len(sorted_array) == 0:
        return -1
    elif type(test_value) != int:
        return -1
    elif test_value not in sorted_array:
        return -1
    else:
        low = 0
        high = len(sorted_array)
        sub_binary_search(sorted_array, test_value, low, high)


if __name__ == '__main__':
    sub_binary_search(range([10, 20, 30, 40, 50, 60], 20))
