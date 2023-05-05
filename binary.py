class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        return self._search_recursive(current_node.right, value)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node
        if value < current_node.value:
            return self._search_recursive(current_node.left, value)
        return self._search_recursive(current_node.right, value)

    def traverse_inorder(self):
        self._traverse_inorder_recursive(self.root)

    def _traverse_inorder_recursive(self, current_node):
        if current_node is not None:
            self._traverse_inorder_recursive(current_node.left)
            print(current_node.value)
            self._traverse_inorder_recursive(current_node.right)


# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print("Inorder traversal:")
tree.traverse_inorder()

print("Search for value 3:")
result = tree.search(3)
if result:
    print("Value found!")
else:
    print("Value not found!")
    def traverse_inorder(self):
        self._traverse_inorder_recursive(self.root)

    def _traverse_inorder_recursive(self, current_node):
        if current_node is not None:
            self._traverse_inorder_recursive(current_node.left)
            print(current_node.value)
            self._traverse_inorder_recursive(current_node.right)


# Example usage:
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print("Inorder traversal:")
tree.traverse_inorder()

print("Search for value 3:")
result = tree.search(3)
if result:
    print("Value found!")
else:
    print("Value not found!")
