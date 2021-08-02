x = "rotator"


def palindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False


def palindromecheck(x):
    x = "#" + x + "@"
    for i in range(1, len(x) - 1):
        for j in range(i, len(x) - 1):
            if palindrome(x[i:j + 1]):
                print(x[i:j + 1])


palindromecheck(x)
