'''
Q. 2 Write a program to perform the following operations on a Linear Queue
        1. Enqueue an element into the queue
        2. Dequeue an element from the queue
        3. Display
        4. Reverse the queue using stack
        5. Merge two queues into one.
        6. Check if two queues are identical
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Lqueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
            current = self.front
            print("Deleted:", current.data)
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            current = None
        else:
            print("Queue is empty")

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next

    # Reverse Queue using Stack
    def reverse_queue(self):
        stack = []
        while self.front:
            current = self.front
            self.front = self.front.next
            stack.append(current.data)
        self.rear = None
        while stack:
            self.enqueue(Node(stack.pop()))

    # Merge Two Queues
    def merge(self, q2):
        if q2.front is None:
            return
        if self.rear:
            self.rear.next = q2.front
            self.rear = q2.rear
        else:
            self.front = q2.front
            self.rear = q2.rear

    # Check Identical Queues
    def identical(self, q2):
        current1 = self.front
        current2 = q2.front
        while current1 and current2:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None

q1 = Lqueue()
q1.enqueue(Node(10))
q1.enqueue(Node(20))
q1.enqueue(Node(30))
q1.enqueue(Node(40))

print("Original Queue:")
q1.display()
print()

q1.dequeue()
print("After Dequeue:")
q1.display()
print()

q1.reverse_queue()
print("Reversed Queue:")
q1.display()
print()

q2 = Lqueue()
q2.enqueue(Node(50))
q2.enqueue(Node(60))

q1.merge(q2)
print("Merged Queue:")
q1.display()
print()

q3 = Lqueue()
q3.enqueue(Node(40))
q3.enqueue(Node(30))
q3.enqueue(Node(20))
q3.enqueue(Node(10))
q3.enqueue(Node(50))
q3.enqueue(Node(60))
if q1.identical(q3):
    print("Queues are identical")
else:
    print("Queues are not identical")