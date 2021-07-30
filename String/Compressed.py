expression = "aaabbccdee"


def compress(array):
    new = ""
    count = 0
    for i in range(len(array)):
        if len(new) == 0:
            new = new + array[i]
            count += 1
        elif array[i] == array[i - 1]:
            count += 1
        else:
            if count == 1:
                pass
            else:
                new = new + str(count)
            count = 1
            new = new + array[i]
    new = new + str(count)
    return new


print(compress(expression))
