class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head


def Traverse(head):
    if head is None:
        print("empty")

    x = head.next
    print(head.key)
    while x != head:
        print(x.key)
        x = x.next


Traverse(head)
print()


def insertbegin(head, key):
    temp = Node(key)
    if head is None:
        return temp
    x = head.next
    while x.next != head:
        x = x.next

    temp.next = head
    x.next = temp
    return temp


head = insertbegin(head, 0)
Traverse(head)
print()


def insertlast(head, key):
    temp = Node(key)
    if head is None:
        return temp
    x = head.next
    while x.next != head:
        x = x.next

    temp.next = x.next
    x.next = temp

    return head


head = insertlast(head, 7)
Traverse(head)
print()


def deletebegin(head):
    if head is None or head.next is None:
        print("None")
    else:
        x = head.next
        while x.next != head:
            x = x.next

        x.next = head.next

        return head.next


head = deletebegin(head)
Traverse(head)
print()


def deletelast(head):
    if head is None or head.next is None:
        print("None")
    else:
        x = head.next
        while x.next.next != head:
            x = x.next

        x.next = head

        return head


head = deletelast(head)
Traverse(head)
print()
