# How to find largest and smallest number in unsorted array

intlist = [12, 56, 1, 2, 3, 4, 1, 23, 26, 14, 85, 13, -6, 1]
largest = intlist[0]
smallest = intlist[-1]
for i in intlist:
    if i != largest:
        if i > largest:
            largest = i
            if i < smallest:
                smallest = i
        elif i < smallest:
            smallest = i

print(largest, smallest)
