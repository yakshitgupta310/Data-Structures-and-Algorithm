x = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]


def morefrequent(x, val1, val2):
    count1 = 0
    count2 = 0
    for i in x:
        if i == val1:
            count1 += 1
        elif i == val2:
            count2 += 1

    if count1 == count2:
        return min(val1, val2)
    elif count1 > count2:
        return val1
    else:
        return val2


print(morefrequent(x, 4, 5))
