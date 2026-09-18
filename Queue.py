from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

value = queue.popleft()

print("Popped value:", value)
print("Remaining queue:", queue)