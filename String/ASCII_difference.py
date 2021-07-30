expression = "abecd"


def ASCII(string):
    new = ""

    new = new + string[0]
    for i in range(1, len(string)):
        value = ord(string[i]) - ord(string[i - 1])
        # print(value)
        new = new + str(value) + string[i]

    return new


print(ASCII(expression))
