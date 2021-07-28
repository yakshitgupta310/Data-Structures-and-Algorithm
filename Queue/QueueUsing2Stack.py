class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        if len(self.s1) == self.capacity:
            print("Overflow")
        else:
            (self.s1).append(val)

    def deque(self):
        if len(self.s1) == 0:
            print("Underflow")
        else:
            while len(self.s1) != 1:
                x = (self.s1).pop()
                (self.s2).append(x)
            deleted = (self.s1).pop()
            while len(self.s2) != 0:
                x = (self.s2).pop()
                (self.s1).append(x)
            print(str(deleted) + " has been deleted from queue")


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
print(q.s1, q.s2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.s1, q.s2)
q.deque()
print(q.s1, q.s2)
q.deque()
print(q.s1, q.s2)
q.deque()
print(q.s1, q.s2)
q.deque()
print(q.s1, q.s2)
q.deque()
print(q.s1, q.s2)
q.deque()
print(q.s1, q.s2)
