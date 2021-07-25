x = [5, 4, 10, 1, 6, 2]


def Selection(x):
    n = len(x)
    for i in range(1, n):
        temp = x[i]
        j = i - 1
        while (j >= 0):
            if x[j] > temp:
                x[j + 1] = x[j]
                j -= 1
            else:
                break

        x[j + 1] = temp
    return x


print(Selection(x))
