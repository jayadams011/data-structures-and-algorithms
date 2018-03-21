def insertShiftArray(array, value):
    if len(array) > 0 and len(array) % 2 == 0:
        middle = len(array)//2
    elif len(array) > 0 and len(array) % 2 == 1:
        middle = len(array)//2 + 1
    else:
        middle = 0
        new_array = [0]*(len(array)+1)
    for i in range(middle):
        new_array[i] = array[i]
        new_array[middle] = value
    for i in range(middle + 1, len(new_array)):
        new_array[i] = array[i-1]
    print(new_array)

    insertShiftArray([10, 20, 40, 50], 35)
