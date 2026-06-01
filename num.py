# create empty queue
queue = []

# number of elements
n = int(input("Enter number of elements: "))

# enqueue
for i in range(n):
    element = int(input("Enter element: "))
    queue.append(element)

print("Queue after insertion:", queue)

# dequeue
if len(queue) == 0:
    print("Queue is empty")
else:
    removed = queue.pop()
    print("Removed element:", removed)

print("Queue after deletion:", queue)