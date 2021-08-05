s = "abccddde"
queries = [1, 3, 12, 5, 9, 10]


def UniformString(s, queries):
    weights = {}
    result = []

    for i in range(len(s)):
        x = i
        while s[i] == s[x]:
            weight = ord(s[i]) - ord("a") + 1
            weight = weight * (x - i + 1)
            weights[weight] = 1
            x += 1
            if x >= len(s):
                break

    for query in queries:
        if query in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result


print(UniformString(s, queries))
