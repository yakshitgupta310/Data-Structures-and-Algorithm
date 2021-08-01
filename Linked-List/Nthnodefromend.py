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
head.next.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next.next = Node(14)
head.next.next.next.next.next.next.next.next.next = Node(25)


def fromend(head, n):
    x = head
    ref = x
    start = x
    for i in range(n):
        ref = ref.next

    while ref is not None:
        start = start.next
        ref = ref.next

    print(start.key)


fromend(head, 3)
