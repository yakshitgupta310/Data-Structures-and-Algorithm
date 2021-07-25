x = [15, 5, 24, 8, 1, 3, 16, 10, 20]


def Merge(x, low, mid, high):
    left = x[low:mid + 1]
    right = x[mid + 1:high + 1]
    l = 0
    r = 0
    k = low
    while (l < len(left)) and (r < len(right)):
        if left[l] < right[r]:
            x[k] = left[l]
            l += 1
            k += 1
        else:
            x[k] = right[r]
            r += 1
            k += 1

    while l < len(left):
        x[k] = left[l]
        l += 1
        k += 1

    while r < len(right):
        x[k] = right[r]
        r += 1
        k += 1

    return x


def MergeSort(x, low, high):
    if low < high:
        mid = (low + high) // 2
        MergeSort(x, low, mid)
        MergeSort(x, mid + 1, high)
        Merge(x, low, mid, high)

    return x


print(MergeSort(x, 0, len(x) - 1))
