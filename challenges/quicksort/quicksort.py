"""Define quicksort finction."""


def quicksort(arr):
    """Quick sort."""
    R = []
    L = []
    pivot_list = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                L.append(i)
            elif i > pivot:
                R.append(i)
            else:
                pivot.append(i)
        R = quicksort(R)
        L = quicksort(L)

    return L + pivot + R
    




