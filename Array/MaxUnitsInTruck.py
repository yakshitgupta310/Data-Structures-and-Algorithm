BoxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
Trucksize = 10


def MaxUnit(Boxtypes, Trucksize):
    Total = 0

    Boxtypes = sorted(Boxtypes, key=lambda x: x[1], reverse=True)

    for box in Boxtypes:
        if Trucksize == 0:
            break
        else:
            if Trucksize > box[0]:
                Total += (box[0] * box[1])
                Trucksize -= box[0]
            else:
                Total += (Trucksize * box[1])
                Trucksize = 0

    print(Total)


MaxUnit(BoxTypes, Trucksize)
