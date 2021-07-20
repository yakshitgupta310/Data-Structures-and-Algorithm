def Binary(arr, x):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        elif arr[mid] == x:
            return mid
    return -1


print(Binary([10, 20, 30, 40, 50, 70], 25))
