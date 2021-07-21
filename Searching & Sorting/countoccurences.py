x = [1, 2, 3, 4, 4, 4, 5, 5, 7, 13]


def counting(arr, x):
    low = 0
    high = len(arr) - 1
    f = None
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or arr[mid] != arr[mid - 1]:
                f = mid
                break
            else:
                f = mid
                high = mid - 1

    if f is None:
        return -1

    l = 0
    h = len(arr) - 1
    g = None
    while l <= h:
        m = (l + h) // 2
        if arr[m] > x:
            h = m - 1
        elif arr[m] < x:
            l = m + 1
        else:
            if (m == len(arr) - 1) or (arr[m + 1] != arr[m]):
                g = m
                break
            else:
                low = m + 1

    return g - f + 1


print(counting([1, 1, 1, 1, 1, 0, 0, 0], 1))
