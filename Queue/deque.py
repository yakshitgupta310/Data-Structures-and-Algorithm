import collections

q = collections.deque(["1", "2", "3"])
print(q)

q.append("4")
q.appendleft("5")
print(q)
q.pop()
print(q)
q.popleft()
print(q)
