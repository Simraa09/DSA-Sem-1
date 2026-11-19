# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List - Insert at end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    # 2. Traverse and print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 3. Insert node after a given value
    def insert_after(self, prev_data, new_data):
        temp = self.head
        while temp:
            if temp.data == prev_data:
                break
            temp = temp.next
        if temp is None:
            print("Node not found")
        else:
            new_node = Node(new_data)
            new_node.next = temp.next
            temp.next = new_node

    # 4. Find Middle Node
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print("Middle node:", slow.data)
        else:
            print("List is empty")

    # 5. Delete Node
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
        else:
            prev = None
            while temp and temp.data != key:
                prev = temp
                temp = temp.next
            if temp is None:
                print("Node not found")
            else:
                prev.next = temp.next
                temp = None

    # 6. Reverse Linked List
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 7. Sum of every two consecutive nodes
    def consecutive_sum(self):
        current = self.head
        while current and current.next:
            total = current.data + current.next.data
            print(current.data, "+", current.next.data, "=", total)
            current = current.next

# Usage
ll = LinkedList()

# 1. Create Linked List
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Original Linked List:")
ll.print_list()

# 2. Insert node
ll.insert_after(20, 25)
print("\nAfter Insertion:")
ll.print_list()

# 3. Find middle node
print("\nMiddle Node:")
ll.find_middle()

# 4. Delete node
ll.delete_node(25)
print("\nAfter Deletion:")
ll.print_list()

# 5. Reverse Linked List
ll.reverse()
print("\nReversed Linked List:")
ll.print_list()

# 6. Sum of consecutive nodes
print("\nSum of Consecutive Nodes:")
ll.consecutive_sum()
