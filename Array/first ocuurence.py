#  x=[1,2,1,4,3,5,6,7]

def first(arr, n, position):
    if len(arr) == 0:
        return -1
    if position >= len(arr):
        return

    if arr[position] == n:
        return position
    else:
        x = first(arr, n, position + 1)
        if x is None:
            return -1
        return x


print(first([1, 2, 1, 4, 3, 5, 6, 7], 10, 0))
