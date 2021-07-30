expression = "aaabbccdee"


def duplicates(string):
    new = ""

    for i in range(len(string)):
        if len(new) == 0:
            new = new + string[i]
        elif string[i] == string[i - 1]:
            pass
        else:
            new = new + string[i]

    return new


print(duplicates(expression))
