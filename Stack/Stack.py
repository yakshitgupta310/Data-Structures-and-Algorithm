class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity
        self.top = None

    def push(self, val):
        if len(self.stack) == self.capacity:
            return "Stack is already Full."
        (self.stack).append(val)
        self.top = val

    def pop(self):
        if not self.stack:
            return "stack is empty."
        (self.stack).pop()
        if not self.stack:
            self.top = None
        else:
            self.top = (self.stack)[-1]

    def size(self):
        return len(self.stack)

    def isempty(self):
        return len(self.stack) == 0


s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.push(5)
print(s.stack)
