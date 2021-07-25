def BubbleSort(x):

    n = len(x)

    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if x[j] > x[j + 1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
                swap = True
        if swap == False:
            return x

    return x


x = [20, 12, 1, 3, 0, 10, 6, 22, 11]

print(BubbleSort(x))
