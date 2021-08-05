s = "GeeksforGeeks"


def FirstNR(s):
    for i in range(len(s)):
        val=s[i+1:].find(s[i])
        if val == -1:
            return s[i]

    return "No such character"


print(FirstNR(s))
