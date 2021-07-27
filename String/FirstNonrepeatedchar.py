# How do you print the first non-repeated character from a string?

b = 'AABBCC'


def Nonrepeated(b):
    counts = {}
    for c in b:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    for i in counts:
        if counts[i] == 1:
            return (i)
    return ("No unique character")


print(Nonrepeated(b))
