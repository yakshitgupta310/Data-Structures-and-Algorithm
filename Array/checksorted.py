x = [1, 2, 3, 5, 4, 6, 7, 8, 9]


def check(array):

    for i in range(1, len(array)):
        if array[i - 1] <= array[i]:
            pass
        else:
            return False

    return True


print(check(x))
