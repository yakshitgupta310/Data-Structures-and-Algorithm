class Cqueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.rear = -1
        self.front = -1
        self.size = 0

    def enqueue(self, key):
        if (self.rear + 1) % self.capacity == (self.front):
            print("Overflow")
        elif self.rear == -1:
            self.rear = 0
            self.front = 0
            self.queue[self.rear] = key
            self.size += 1
        else:
            self.rear = (self.rear + 1) % (self.size)
            self.queue[self.rear] = key
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Underflow")
        else:
            self.queue[self.front] = None
            self.front += 1
            self.size -= 1


x = Cqueue(5)
x.enqueue(1)
x.enqueue(2)
print(x.queue)
x.enqueue(3)
x.enqueue(4)
x.enqueue(5)
print(x.queue)
x.enqueue(6)
print(x.queue)
x.dequeue()
print(x.queue)
x.enqueue(7)
print(x.queue)
x.enqueue(8)
