x = "((a+b)+(c))"


def pop(x, i):
    count = 0
    while x[-1] != i:
        x.pop()
        count += 1
    x.pop()

    return count


def duplicacy(x):
    stack = []

    for i in x:
        if i in ["}", "]", ")"]:
            if i == "}":
                count = pop(stack, "{")
            elif i == "]":
                count = pop(stack, "[")
            else:
                count = pop(stack, "(")
            if count == 0:
                return False
        else:
            stack.append(i)

    return True


print(duplicacy(x))
