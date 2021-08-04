words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"


def Find(words, chars):
    char = {}

    for i in chars:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1

    for word in words:
        x = char.copy()
        y = 0

        for j in word:
            if j not in x:
                break
            else:
                x[j] -= 1
                y += 1
                if x[j] == 0:
                    x.pop(j)

        if y == len(word):
            print(word)


Find(words, chars)
