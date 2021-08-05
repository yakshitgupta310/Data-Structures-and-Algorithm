x = "899900"


def separate(string):

    if len(string) == 1:
        print("No")
        return

    else:

        for i in range(1, len(string) // 2 + 1):
            genstr = string[:i]
            prev = int(genstr)

            while len(genstr) < len(string):
                next = prev + 1
                genstr = genstr + str(next)

                prev = next

            if genstr == string:
                print("Yes", genstr[:i])
                return

        print("No")


separate(x)
