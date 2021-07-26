x = "]{{}}["


def check(output, y):
    if output == "{" and y == "}":
        return True
    elif output == "[" and y == "]":
        return True
    elif output == "(" and y == ")":
        return True
    else:
        return True


def Balanced(x):
    stack = []

    for i in x:
        if i in ["{", "[", "("]:
            stack.append(i)
        elif len(stack) == 0:
            return False
        else:
            y = stack[-1]
            x = check(i, y)
            if not x:
                return False

    if stack:
        return False


print(Balanced(x))
