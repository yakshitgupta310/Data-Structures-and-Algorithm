x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def Minimum(stack):
    min = None

    while stack:
        y = stack.pop()
        if min is None:
            # print(min)
            min = y
        elif y < min:
            # print(min)
            min = y

    return min


print(Minimum(x))
