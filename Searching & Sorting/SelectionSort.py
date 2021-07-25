def SelectionSort(x):

    n = len(x)
    for i in range(n):
        a = i
        for j in range(i, n):
            if x[a] > x[j]:
                a = j

        temp = x[a]
        x[a] = x[i]
        x[i] = temp

    return x


x = [20, 12, 1, 3, 0, 10, 6, 22, 11]

print(SelectionSort(x))
