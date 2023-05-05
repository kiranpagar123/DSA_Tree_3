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

    def traverse_preorder(self):
        self._traverse_preorder_recursive(self.root)

    def _traverse_preorder_recursive(self, current_node):
        if current_node is not None:
            print(current_node.value)
            self._traverse_preorder_recursive(current_node.left)
            self._traverse_preorder_recursive(current_node.right)

    def traverse_inorder(self):
        self._traverse_inorder_recursive(self.root)

    def _traverse_inorder_recursive(self, current_node):
        if current_node is not None:
            self._traverse_inorder_recursive(current_node.left)
            print(current_node.value)
            self._traverse_inorder_recursive(current_node.right)

    def traverse_postorder(self):
        self._traverse_postorder_recursive(self.root)

    def _traverse_postorder_recursive(self, current_node):
        if current_node is not None:
            self._traverse_postorder_recursive(current_node.left)
            self._traverse_postorder_recursive(current_node.right)
            print(current_node.value)
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)

print("Pre-order traversal:")
tree.traverse_preorder()

print("In-order traversal:")
tree.traverse_inorder()

print("Post-order traversal:")
tree.traverse_postorder()
