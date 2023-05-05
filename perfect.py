class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def sum_nodes(root):
    if not root:
        return 0
    total_nodes = count_nodes(root)
    return total_nodes * root.val
# create a perfect binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# find the sum of all nodes
sum = sum_nodes(root)

# print the result
print(sum)  # output: 56
