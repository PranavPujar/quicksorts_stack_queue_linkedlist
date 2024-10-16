# PRANAV UMAKANT PUJAR 1001965075

# Constants
MAX_SIZE = 10

class Stack:
    def __init__(self):
        self.stack = [0] * MAX_SIZE
        self.top = -1
    
    def push(self, item):
        if not isinstance(item, int):
            raise TypeError("Only integers are allowed")
        if self.top >= MAX_SIZE - 1:
            raise IndexError("Stack overflow")
        self.top += 1
        self.stack[self.top] = item
    
    def pop(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        item = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
        return item
    
    def peek(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

# Example Usage for Testing - Integers only
stack = Stack()
stack.push(4)
stack.push(5)
print("Stack after push:", stack.stack)
stack.pop()
print("Stack after pop:", stack.stack)