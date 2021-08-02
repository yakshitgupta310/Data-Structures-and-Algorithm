s1 = "gkabcgkdefgk"
s2 = "gk"


def pattern(s1, s2):
    found = None
    i = 0

    while found != -1:
        found = s1.find(s2, i)
        print(found)
        i = found + 1


pattern(s1, s2)
