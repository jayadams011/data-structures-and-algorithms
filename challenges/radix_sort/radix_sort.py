"""Define function to sort  an unsorted array using radix_sort."""
import math


def radix_sort(arr):
    """Define radix sort."""
    maxLen = -1
    for num in arr:
        numLen = int(math.log10(num)) + 1
        if numLen > maxLen:
            maxLen = numLen
    for val in range(0, maxLen):
        buckets = [[] for i in range(0, 10)]
        for number in arr:
            buckets[number // 10**val % 10].append(number)
        arr = []
        for bucket in buckets:
            for num in bucket:
                arr.append(num)
    return arr
