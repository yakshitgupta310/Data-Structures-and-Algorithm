class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(10)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(12)
head.next.next.next.next.next.next = Node(0)
head.next.next.next.next.next.next.next = Node(0)
head.next.next.next.next.next.next.next.next = Node(1)
head.next.next.next.next.next.next.next.next.next = Node(20)


def removeduplicates(head):
    if head is None or head.next is None:
        return head
    val = []
    x = head
    while x != None:
        if x.key not in val:
            val.append(x.key)
            temp = x
            x = x.next
        else:
            temp.next = x.next
            x = x.next

    return head


def Travesrse(head):
    x = head
    while x != None:
        print(x.key, end=" ")
        x = x.next


Travesrse(head)
head = removeduplicates(head)
print()
Travesrse(head)
