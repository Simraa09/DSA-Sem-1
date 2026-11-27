
# Node Class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# BST Class
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)

        if not self.root:
            self.root = new_node
            return

        current = self.root
        parent = None

        while current:
            parent = current

            if key < current.key:
                current = current.left
            else:
                current = current.right

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node


# Main Program
bst = BST()

for x in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(x)

print("BST Insertion Completed")
