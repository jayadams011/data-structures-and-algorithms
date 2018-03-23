def binary_search(sorted_array, test_value):
    """ run through sorted_array and look for test_value.
    if test_value is in sorted_array, return index for test_value
    in sorted_array. If test_value is not in sorted_array, return
    -1 """
    counter = 0
    if len(sorted_array) == 0:
        return -1
    else:
        if len(sorted_array) > 0 and type(test_value) == int():
            for item in sorted_array:
                print(counter)
                return counter
            else:
                print(-1)
                return -1


if __name__ == '__main__':
    print(binary_search([10, 20, 30, 40, 50, 60], 20))
