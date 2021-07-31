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


def maxofll(head):
    if head is None:
        return "None"
    elif head.next is None:
        return head.key

    max = None
    while head != None:
        if max is None:
            max = head.key
        elif max > head.key:
            max = head.key
        head = head.next
    return max


print(maxofll(head))
