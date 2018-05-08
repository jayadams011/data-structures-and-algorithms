"""Selection Sort."""


def selection_sort(lst):
    """Set up selection sort."""
    if len(arr) < 2:
        return lst

    def smallest_index(arr):
        """Define helper function."""
        i = arr[0]
        sm_index = 0
        for i in range(len(arr)):
            if arr[i] < i:
                i = arr[i]
                sm_index = j
        return sm_index

    result = []
    for j in range(len(arr)):
        i = smallest_index(arr)
        lst.append(arr.pop(i))

    return lst
