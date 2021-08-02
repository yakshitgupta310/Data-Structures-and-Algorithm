x = "RLRRLLRLRL"


def balanced(x):
    balance = None
    start = 0

    for i in range(len(x)):
        if x[i] == "R":
            if balance is None:
                balance = 1
            else:
                balance += 1

        elif x[i] == "L":
            if balance is None:
                balance = -1
            else:
                balance -= 1

        if balance == 0:
            print(x[start:i + 1])
            start = i + 1


balanced(x)
