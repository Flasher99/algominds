from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if len(self.q) == 0:
            print("Stack is Empty")
        else:
            print("Popped:", self.q.popleft())

    def display(self):
        print("Stack:", list(self.q))


# Create object outside loop
s = Stack()

while True:
    print("\n1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        s.push(val)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        break