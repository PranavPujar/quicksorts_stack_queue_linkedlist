# PRANAV UMAKANT PUJAR 1001965075

# Constants
MAX_SIZE = 10


class Queue:
    def __init__(self):
        self.queue = [0] * MAX_SIZE
        self.front = self.rear = -1
    
    def enqueue(self, item):
        if not isinstance(item, int):
            raise TypeError("Only integers are allowed")
        if (self.rear + 1) % MAX_SIZE == self.front:
            raise IndexError("Queue overflow")
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % MAX_SIZE
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            raise IndexError("Queue underflow")
        item = self.queue[self.front]
        self.queue[self.front] = 0
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % MAX_SIZE
        return item

    def is_empty(self):
        return self.front == -1


# Example Usage for Testing - Integers only
queue = Queue()
queue.enqueue(12)
queue.enqueue(32)
print("Queue after enqueue:", queue.queue)
queue.dequeue()
print("Queue after dequeue:", queue.queue)


