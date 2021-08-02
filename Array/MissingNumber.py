x = [i for i in range(1, 101)]
x.remove(50)

def missing(x):

    for i in range(1, 101):
        if i in x:
            pass
        else:
            return (str(i) + " not found in the array.")

    return "All values present in the array."


print(missing(x))
