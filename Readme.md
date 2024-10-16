# Data Structures and Quickselect Algorithm

This project contains implementations of basic data structures and the Quickselect algorithm in Python, adhering to fixed-size integer array constraints.

### Quickselect Algorithm
Finds the i-th smallest element in an array.
- **Function:** `find_ith_smallest(arr, start, end, target_rank)`
- **Arguments:** 
  - `arr`: Array of integers.
  - `start`: Start index.
  - `end`: End index.
  - `target_rank`: Desired order statistic.
- **Example:** `find_ith_smallest([12, 3, 5, 7], 0, 3, 2)` returns 5 (2nd smallest).

### Stack
A Last In, First Out (LIFO) structure.
- **Methods:**
  - `push(item)`: Adds item to top.
  - `pop()`: Removes top item.
  - `peek()`: Returns top item.
  - `is_empty()`: Checks if stack is empty.

### Queue
A First In, First Out (FIFO) structure using a circular array.
- **Methods:**
  - `enqueue(item)`: Adds item to end.
  - `dequeue()`: Removes front item.
  - `is_empty()`: Checks if queue is empty.

### Singly Linked List
A basic linked list using fixed-size arrays.
- **Methods:**
  - `insert(item)`: Adds item to start.
  - `delete()`: Removes first item.
  - `display()`: Prints list contents.

### Usage Example
```python
stack = Stack()
stack.push(1)
stack.pop()
queue = Queue()
queue.enqueue(1)
queue.dequeue()
linked_list = SinglyLinkedList()
linked_list.insert(1)
linked_list.display()
find_ith_smallest([10, 4, 5, 8], 0, 3, 3)
```

---