class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DCLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def insert_at_position(self, position, value):
        """Insert value at a 1-based position in the circular list."""
        if position < 1:
            raise IndexError("Position must be 1 or greater")

        new_node = Node(value)
        if self.head is None:
            if position != 1:
                raise IndexError("Position out of range")
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        if position == 1:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 2):
            current = current.next
            if current == self.head:
                raise IndexError("Position out of range")

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

    def delete_at_position(self, position):
        """Delete and return the value at a 1-based position."""
        if self.head is None or position < 1:
            raise IndexError("Position out of range")

        current = self.head
        for _ in range(position - 1):
            current = current.next
            if current == self.head:
                raise IndexError("Position out of range")

        if current.next == current:
            self.head = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            if current == self.head:
                self.head = current.next

        return current.data

    def print(self):
        if self.head is None:
            print("The list is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

list1 = DCLL()
n1 = Node(10)
n2 = Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()