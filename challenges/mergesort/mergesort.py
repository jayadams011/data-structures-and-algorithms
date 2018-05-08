"""Define function to sort and merge an unsorted array"""


def mergersort(arr):
    """Sort function."""
    def split(arr):
        if len(arr) <= 1:
            return lst

        mid = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        left = split(left)
        right = split(right)
        return merge(left, right)

    def merge(left, right):
        """Define helper Function."""
        temp = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                temp.append(left.pop(0))
            else:
                temp.append(right.pop(0))

        while len(left) > 0:
            temp.append(left.pop(0))
        while len(right) > 0:
            temp.append(right.pop(0))

        return temp

    return split(arr)
