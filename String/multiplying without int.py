
s1 = "436"
s2 = "-"
x = []
y = []
for i in range(len(s1)):
    s = int(s1[i]) % 10
    s = str(s) + ("0" * (len(s1) - 1 - i))
    x.append(s)

for i in range(len(s2)):
    s = int(s2[i]) % 10
    s = str(s) + "0" * (len(s2) - i - 1)
    y.append(s)

z = 0
for i in range(-1, -(len(y) + 1), -1):
    k = 0
    for j in range(-1, -(len(x) + 1), -1):
        k = (int(y[i]) * int(x[j]))
        z += k


# print(z)
