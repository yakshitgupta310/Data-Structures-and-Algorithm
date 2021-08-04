nums = [1, 2, 3, 1, 1, 3]


def GoodPair(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                print(i, j)


GoodPair(nums)
