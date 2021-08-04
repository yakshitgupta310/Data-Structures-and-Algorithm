x = [3, 5, 2, 1, 0, 4]


def Replace(x):
    result = [None] * len(x)
    hash = {}

    for i in range(len(x)):
        result[x[i]] = i

    return result


print(Replace(x))
