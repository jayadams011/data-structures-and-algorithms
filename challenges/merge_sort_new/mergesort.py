"""Define function to sort and merge an unsorted array."""


def mergesort(arr):
    """Define merge sort."""
    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]
    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)

    lst = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        elif left[i] > right[j]:
            lst.append(right[j])
            j += 1
        else:
            lst.append(left[i])
            lst.append(right[j])
            i += 1
            j += 1

    for _ in range(i, len(left)):
        lst.append(left[_])
    for _ in range(j, len(right)):
        lst.append(right[_])

    return lst
