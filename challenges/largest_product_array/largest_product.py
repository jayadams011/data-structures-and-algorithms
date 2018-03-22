def largest_product(arr):
    """
    Write a function which takes a 2D array and returns the largest product of
    2 adjacent values.
    """
    largest = 0

    if len(arr)







def insertShiftArray(old_array, value):
    if len(old_array) > 0 and len(old_array) % 2 == 0:
        middle = len(old_array)//2
    elif len(old_array) > 0 and len(old_array) % 2 == 1:
        middle = len(old_array)//2 + 1
    else: