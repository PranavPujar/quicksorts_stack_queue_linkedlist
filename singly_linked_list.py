# PRANAV UMAKANT PUJAR 1001965075

# Constants
MAX_SIZE = 10

class SinglyLinkedList:
    def __init__(self):
        self.list = [0] * MAX_SIZE
        self.next = [-1] * MAX_SIZE
        self.head = -1
        self.free = 0
        for i in range(MAX_SIZE - 1):
            self.next[i] = i + 1
        self.next[MAX_SIZE - 1] = -1
    
    def insert(self, item):
        if not isinstance(item, int):
            raise TypeError("Only integers are allowed")
        if self.free == -1:
            raise IndexError("List overflow")
        new_node = self.free
        self.free = self.next[new_node]
        self.list[new_node] = item
        self.next[new_node] = self.head
        self.head = new_node
    
    def delete(self):
        if self.head == -1:
            raise IndexError("List underflow")
        removed = self.head
        self.head = self.next[removed]
        self.list[removed] = 0
        self.next[removed] = self.free
        self.free = removed
    
    def display(self):
        temp = self.head
        while temp != -1:
            print(self.list[temp], end=" -> ")
            temp = self.next[temp]
        print("None")


# Example Usage for Testing - Integers only
linked_list = SinglyLinkedList()
linked_list.insert(33)
linked_list.insert(44)
linked_list.display()
linked_list.delete()
linked_list.display()