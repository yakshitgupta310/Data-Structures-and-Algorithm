x = [4, 67, 13, 12, 15]


def ImmediateSmaller(x, val):
    min = None
    for i in x:
        if i < val:
            if min is None:
                min = i
            elif min < i:
                min = i

    if min is None:
        return -1
    return min


print(ImmediateSmaller(x, 5))
