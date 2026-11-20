'''
Q. 1 Create a Stack with following operations
        1. Push
        2. Pop
        3. Display
        4. Reverse String using Stack
        5. Reverse Stack using another Stack
'''

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
            print("Stack is empty")
        else:
            current = self.top
            self.top = self.top.next
            print("Popped:", current.data)
            current = None

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next

    # Reverse String using Stack
    def reverse_string(self, s):
        current = []
        for i in s:
            current.append(i)
        rev = ""
        while current:
            rev += current.pop()
        print("Reversed String:", rev)

    # Reverse Stack using another Stack
    def reverse_stack(self):
        current_stack = Stack()
        while self.top:
            current = self.top
            self.top = self.top.next
            current.next = current_stack.top
            current_stack.top = current
        self.top = current_stack.top

s1 = Stack()
s1.push(Node(10))
s1.push(Node(20))
s1.push(Node(30))
s1.push(Node(40))

print("Original Stack:")
s1.display()
print()

s1.pop()
print("After Pop:")
s1.display()
print()

s1.reverse_string("Hello World!")
s1.reverse_stack()
print("Reversed Stack:")
s1.display()
print()
