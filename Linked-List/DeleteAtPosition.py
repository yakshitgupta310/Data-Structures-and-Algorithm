class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(7)


def Deletepos(head, pos):
    if head == None:
        return "Empty ll"
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
            temp = x.next.next
            x.next = temp
            return "Deleted"
        else:
            return "LL not long enough"


print(Deletepos(head, 6))
x = head
while x != None:
    print(x.key)
    x = x.next
