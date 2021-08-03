x = "eHello123@"
# x = "hella"


def validation(string):
    if len(string) < 10:
        return 0
    num = 0
    special = 0
    up = 0
    low = 0
    for i in string:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            num = 1
        elif i in ["@", "#", "$", "-", "*"]:
            special = 1
        elif i.upper() == i:
            up = 1
        elif i.lower() == i:
            low = 1

    if num == 0 or special == 0 or up == 0 or low == 0:
        return 0
    return 1


print(validation(x))
