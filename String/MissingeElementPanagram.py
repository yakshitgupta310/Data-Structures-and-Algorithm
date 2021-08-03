x = "abcdefghijklmnopqrsuvwxy"


def Missing(string):
    alphabets = [None] * 26

    for i in string:
        val = ord(i) - ord("a")
        if alphabets[val] != None:
            continue
        alphabets[val] = 1

    remaining = []
    for i in range(len(alphabets)):
        if alphabets[i] == None:
            remaining.append(chr(i + ord("a")))

    return remaining


print(Missing(x))
