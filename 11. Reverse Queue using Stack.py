
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        temp = self.top
        self.top = self.top.next
        data = temp.data
        temp = None
        return data

    def is_empty(self):
        return self.top is None


class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, element):
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        temp = self.front
        data = temp.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def is_empty(self):
        return self.front is None

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def reverse_queue(q1):
    st1 = Stack()

    # Step 1: Queue to Stack
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))

    # Step 2: Stack to Queue
    while not st1.is_empty():
        q1.enqueue(st1.pop())


# Create a queue
myQueue = LQueue()

myQueue.enqueue(11)
myQueue.enqueue(58)
myQueue.enqueue(22)

print("Original Queue:", end=" ")
myQueue.printQueue()

reverse_queue(myQueue)

print("Reversed Queue:", end=" ")
myQueue.printQueue()
