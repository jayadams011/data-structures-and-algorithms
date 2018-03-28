def largest_product(arr):
    """
    Write a function which takes a 2D array and returns the largest product of
    2 adjacent values.
    """
    if not arr:
        return 'empty arr'
    largest_prod = 0
    product = 0
    for index in arr:
        product = index[0] * index[1]
        if product > largest_prod:
            largest_prod = product
    return largest_prod
