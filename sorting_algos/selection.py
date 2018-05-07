"""Selection Sort."""


def selection_sort(arr):
    """Set up selection sort."""
    for i in range(len(arr)-1, 0, -1):
        index_max_val = 0
        for j in range(1, i + 1):
            if arr[location] > arr[index_max_val]:
                index_max_val = j
