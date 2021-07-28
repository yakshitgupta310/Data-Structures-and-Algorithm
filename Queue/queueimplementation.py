class Queue:
    def __init__(self, length):
        self.length = length
        self.queue = [None] * self.length
        self.size = 0
        self.front = None

    def enqueue(self, data):
        if self.size < (self.length):
            if self.front is None:
                self.front = 0
                (self.queue)[self.front] = data
                self.size += 1
                print(self.queue)
            else:
                self.queue[(self.size)] = data
                self.size += 1
                print(self.queue)
        else:
            print("Queue is full.")

    def dequeue(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            y = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            self.size -= 1
            print(str(y) + " has been removed.")
            print(self.queue)

    def Size(self):
        print("Length of queue is " + str(self.size))

    def Front(self):
        print(self.queue[self.front])

    def Rear(self):
        print((self.queue)[(self.size) - 1])


q = Queue(5)
q.enqueue(10)
q.Size()
q.enqueue(20)
q.Size()
q.enqueue(30)
q.Size()
q.enqueue(40)
q.Size()
q.enqueue(50)
q.Size()
q.enqueue(60)
q.Size()
q.Front()
q.Rear()
q.dequeue()
q.Size()
q.Front()
q.Rear()
q.dequeue()
q.Size()
q.dequeue()
q.Size()
q.dequeue()
q.Size()
q.dequeue()
q.Size()
