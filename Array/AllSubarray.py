x="abcd"

for i in range(len(x)):
    for j in range(i, len(x)):
        print(x[i:j+1])
