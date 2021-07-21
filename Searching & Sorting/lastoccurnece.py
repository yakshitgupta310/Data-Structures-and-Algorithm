def last(arr, x):
    low = 0
    high = len(arr) - 1
    f = None
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            if mid != (len(arr) - 1):
                if f is None:
                    f = mid
                else:
                    if arr[mid + 1] == x:
                        low = mid + 1
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


print(last([1, 1, 1, 1, 1, 0, 0, 0], 1))

arr = [1, 2, 3]
n = len(arr)

for i in range(1, n - 1):
    print(arr[i], end=" ")
    if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
        print(i)
    else:
        print("No")
if arr[n - 1] > arr[n - 2]:
    print(n - 1)
elif arr[0] > arr[1]:
    print(0)
