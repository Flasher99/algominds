from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.q1.popleft()

    def top(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.q1[0]

    def isEmpty(self):
        return len(self.q1) == 0


# Driver Code
s = Stack() 

s.push(5)
s.push(15)
s.push(25)

print("Top:", s.top())
print("Pop:", s.pop())
print("Top:", s.top())