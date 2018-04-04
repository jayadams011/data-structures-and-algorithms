def largest_product(arr):
    """
    Write a function which takes a 2D array and returns the largest product of
    2 adjacent values. first function runs the other two through it.
    """
    largest = 0
    if len(arr) == 0:
        return largest
    # if len(arr) == 1:
        #     return largest_product_array(arr[0], largest)
        # for i in range(len(arr) - 1):
        #     largest = largest_product_array(arr[i], largest)
        #     largest = adjacent_products([i]), length)
        #         return largest

        def largest_product_array(arr, largest):
            """ tests largest against inner arrays on first level """
            temp_largest = arr[0] * arr[1] > largest
            if temp_largest > largest:
                return temp_largest
            return largest

        def adjacent_products(arr1, arr2, largest):
            """" tests next level down arrays agains largest """
            temp1 = arr1[0] * arr2[0]
            temp2 = arr1[1] * arr2[1]
            if temp1 > largest and temp1 > temp2:
                return temp1
            elif temp2 > largest and temp 2 > temp1:
                return temp2
            return largest

    # largest = 0
    # if len(arr) == 0:
    #     return largest
    if len(arr) == 1:
        return largest_product_array(arr[0], largest)
    for i in range(len(arr) - 1):
        largest = largest_product_array(arr[i], largest)
        largest = adjacent_products([i]), length)
            return largest
