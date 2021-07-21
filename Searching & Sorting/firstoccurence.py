
def first(arr, x):
    low = 0
    high = len(arr) - 1
    f = None
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            if mid != 0:
                if f is None:
                    f = mid
                else:
                    if arr[mid - 1] == x:
                        high = mid - 1
                    else:
                        return mid
            else:
                return mid
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    if f is None:
        return -1
    else:
        return f


print(first([1, 1, 1, 1, 1, 0, 0, 0], 1))
