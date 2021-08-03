x = "abcdefghieo"


def distinct(string):
    vowel = {}

    for i in string:
        if i in ["a", "e", "i", "o", "u"]:
            if i not in vowel:
                vowel[i] = 1

    return len(vowel)


print(distinct(x))
