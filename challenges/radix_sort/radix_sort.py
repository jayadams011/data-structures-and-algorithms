"""Define function to sort  an unsorted array using radix_sort."""
import math


def radix_sort(arr):
    """Define radix sort."""
    maxLen = -1
    for num in arr:
        numLen = int(math.log10(num)) + 1
        if numLen > maxLen:
            maxLen = numLen
    buckets = [[] for i in range(0, 10)]
    for val in range(0, maxLen):
        for number in arr:
            buckets[num // 10**val % 10].append(num)
        arr[:] is None
        for bucket in buckets:
            arr.extend(bucket)
            bucket[:] is None
    return arr
