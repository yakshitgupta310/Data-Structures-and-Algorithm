class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.pre = None


temp1 = Node(1)
temp2 = Node(2)
temp3 = Node(3)
temp4 = Node(4)
temp5 = Node(5)

temp1.next = temp2
temp2.pre = temp1
temp2.next = temp3
temp3.pre = temp2
temp3.next = temp4
temp4.pre = temp3
temp4.next = temp5
temp5.pre = temp4


def traverseforward(temp1):
    x = temp1
    while x is not None:
        print(x.key)
        x = x.next


def traversebackward(temp4):
    x = temp4
    while x is not None:
        print(x.key)
        x = x.pre


def insertbegin(head, key):
    temp = Node(key)
    temp.next = head
    head.pre = temp

    return temp


def insertlast(head, key):
    temp = Node(key)
    x = head
    while x.next != None:
        x = x.next

    x.next = temp
    temp.pre = x

    return head


def deletebegin(head):
    return head.next


def deletelast(head):
    x = head
    while x.next.next != None:
        x = x.next

    x.next = None
    return head


traverseforward(temp1)
print()
traversebackward(temp5)
print()
head = insertbegin(temp1, 0)
traverseforward(head)
print()
head = insertlast(head, 6)
traverseforward(head)
print()
head = deletebegin(head)
traverseforward(head)
print()
head = deletelast(head)
traverseforward(head)
print()
