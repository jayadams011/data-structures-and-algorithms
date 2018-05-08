"""Define function to sort and merge an unsorted array"""


def mergesort(arr):

    def spilt(arr):
        """Define split func."""
        if len(arr) <= 1:
            return lst

        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        left_half = split(left_half)
        right_half = split(right_half)
        return temp(left_half, right_half)

    def merge(left_half, right_half):
        """Define helper."""
        new_arr = []
        while len(left_half) > 0 and len(right_half) > 0:
            if left_half[0] <= right_half[0]:
                new_arr.append(left_half.pop(0))
            else:
                new_arr.append(right_half.pop(0))

        while len(left) > 0:
            new_arr.append(left_half.pop(0))
        while len(right_half) > 0:
            new-arr.append(right_half.pop(0))

        return new_arr

    return split(arr)
