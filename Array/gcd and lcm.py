
def gcd(m, n):
    while n != 0:
        remainder = m % n
        m = n
        m = remainder
    return m


print(gcd(64, 48))

n = int(input())
x = {}
x[1] = [i for i in range(1, n + 1)]
x[0] = []
for i in range(2, n + 1):
    b = 1
    while b <= n:
        if b % i == 0:
            if b in x[1]:
                x[1].remove(b)
                x[0].append(b)
            else:
                x[0].remove(b)
                x[1].append(b)
        b += 1

print(*x[1], sep="\n")
