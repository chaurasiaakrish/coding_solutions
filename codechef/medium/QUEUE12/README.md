# QUEUE12

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Enqueue and Dequeue Functions
### Enqueue(int item) Function:
- Adds an element to the rear of the queue.
- If the queue is full, it prints an error message and does not enqueue the element.
- Otherwise, it circularly increments the rear index, assigns the item to the updated rear index, and increments currentSize.
### Dequeue() Function:
- Removes an element from the front of the circular queue.
- If the queue is empty, it prints an error message and returns a sentinel value (-1 in this case, which can be considered as an error value).
- Otherwise, it retrieves the item at the front index, circularly increments the front index, decrements currentSize, and returns the removed item.
### Video Explanation
### Task
- You are given implementation of queue.
- There are some dashes, Fill the dashes present in the enqueue and dequeue function.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-01T23:28:07.414Z  

```py
class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.a = [0] * max_size
        self.front = 0
        self.rear = -1
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.current_size == self.max_size

    def size(self):
        return self.current_size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.max_size  # Circular increment
        self.a[self.rear] = item
        self.current_size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return -1  # Return a sentinel value or throw an exception
        removed_item = self.a[self.front]
        self.front = (self.front + 1) % self.max_size  # Circular increment
        self.current_size -= 1
        return removed_item


if __name__ == "__main__":
    n = 10
    #  write your code here
    

```

---

[View on CodeChef](https://www.codechef.com/problems/QUEUE12)