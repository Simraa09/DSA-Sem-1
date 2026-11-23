
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped element:", temp.data)
            self.top = self.top.next
            temp = None

    def print(self):
        temp = self.top
        print("Stack elements:")
        while temp:
            print(temp.data)
            temp = temp.next


# Create a stack
s1 = Stack()

# Push elements
s1.push(Node(10))
s1.push(Node(99))
s1.push(Node(45))
s1.push(Node(67))
s1.push(Node(90))

# Display stack
s1.print()

# Pop an element
s1.pop()

# Display stack after pop
print("\nStack after pop:")
s1.print()
