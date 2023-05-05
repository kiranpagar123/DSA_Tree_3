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

    def height(self):
        return self._calculate_height(self.root)

    def _calculate_height(self, current_node):
        if current_node is None:
            return -1  # Base case for an empty tree

        left_height = self._calculate_height(current_node.left)
        right_height = self._calculate_height(current_node.right)

        # Return the maximum height between the left and right subtrees
        return max(left_height, right_height) + 1
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

tree_height = tree.height()
print("Height of the tree:", tree_height)
