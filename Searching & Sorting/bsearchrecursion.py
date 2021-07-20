def bsearch(arr, x, low, high):
    if low > high:
        return

    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        high = mid - 1
        return bsearch(arr, x, low, high)
    else:
        low = mid + 1
        return bsearch(arr, x, low, high)


f = [10, 20, 30, 40, 50, 70, 80]
print(bsearch(f, 30, 0, len(f) - 1))
