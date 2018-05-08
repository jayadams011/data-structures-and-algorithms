"""Define quicksort finction."""


def quicksort(data):
    """Quick sort."""
    if len(data) < 1:
        return data
    pivot = data[0]
    left = []
    right = []
    for x in range(1, len(data)):
        if data[x] <= pivot:
            left.append(data[x])
        else:
            right.append(data[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right
