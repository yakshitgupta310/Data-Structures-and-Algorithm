# How to find duplicate number on Integer array .


intlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]

n = len(intlist)
listsum = ((n - 1) * n) / 2

diff = sum(intlist) - listsum

print(int(diff))
