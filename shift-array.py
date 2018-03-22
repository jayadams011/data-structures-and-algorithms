def insertShiftArray(old_array, value):
    if len(old_array) > 0 and len(old_array) % 2 == 0:
        middle = len(old_array)//2
    elif len(old_array) > 0 and len(old_array) % 2 == 1:
        middle = len(old_array)//2 + 1
    else:
        middle = 0
    new_array = [0]*(len(old_array)+1)
    for i in range(middle):
        new_array[i] = old_array[i]
    new_array[middle] = value
    for i in range(middle + 1, len(new_array)):
        new_array[i] = old_array[i-1]
    print(new_array)


insertShiftArray([10, 20, 40, 50], 35)
