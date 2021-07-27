# How do you check if two strings are a rotation of each other?

a = "programming"
b = "ingprogramm"
s = "ingprogrammingprogramm"


def check(a, b):
    if len(a) != len(b):
        return False
    else:
        s = b + b
        if b in s:
            return True
        else:
            return False


print(check(a, b))
