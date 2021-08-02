intlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]


def duplicate(array):

    for i in range(len(array)):
        if array[i] in array[:i]:
            return array[i]

    return "No duplicate"


print(duplicate(intlist))
