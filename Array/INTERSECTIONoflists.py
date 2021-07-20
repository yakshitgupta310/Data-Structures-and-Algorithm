# Intersection of two lists.


l1 = [21, 34, 41, 22, 35]
l2 = [61, 34, 45, 21, 11]

intersection = []
for i in l1:
    if i in l2:
        intersection.append(i)

print(intersection)
