"""Define function to sort and merge an unsorted array"""


def mergersort(arr)
"""Define sort function."""

if len(arr) > 2:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        mergeSort(left_arr)
        mergeSort(right_arr)
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
            else:
                arr[k] = right_arr[j]
                j = j+1
            k = k+1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1

        while j < len(right_arr):
            alist[k] = right_arr[j]
            j = j + 1
            k = k + 1
        return mergesort
