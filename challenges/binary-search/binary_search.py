def binary_search(arr, x):
    """ run through sorted_array and look for test_value.
    if test_value is in sorted_array, return index for test_value
    in sorted_array. If test_value is not in sorted_array, return
    -1 """

    if len(arr) == 0:
        return -1
    
    if not isinstance(int, x):
        raise TypeError('x must be an integer')

    start = 0
    end = len(arr) - 1
    mid = len(arr) // 2
    # print(start, end, mid)

    while start + 1 != end:
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid
        elif arr[mid] < x:
            start = mid
        mid = ((end-start)//2) + start

    return -1


if __name__ == '__main__':
    pass
