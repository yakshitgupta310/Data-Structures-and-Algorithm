s1 = "acab"
s2 = "aacb"


def ANagramcheck(s1, s2):
    """
    for i in s1:
        if i in s2:
            s2.remove(i)
            pass
        else:
            return("No")
    return ("Yes")
    """
    if len(s1) != len(s2):
        return(False)
    count = [0] * 256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1

    for x in count:
        if x != 0:
            return (False)

    return(True)


print(ANagramcheck(s1, s2))
