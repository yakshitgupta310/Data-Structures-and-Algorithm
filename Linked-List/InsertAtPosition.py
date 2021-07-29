class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def Insertpos(head, pos, key):
    if head is None:
        return "LL is empty"
    else:
        x = head
        i = 1
        while x != None:
            if i == (pos - 1):
                break
            else:
                i += 1
                x = x.next

        if i == (pos - 1):
            temp = Node(key)
            temp.next = x.next
            x.next = temp
            return "Node inserted at pos"

        else:
            return "LL not long enough"


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
# head.next.next.next.next = Node(6)


print(Insertpos(head, 5, 5))
x = head
while x != None:
    print(x.key)
    x = x.next
