class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_nodes_at_odd_levels(root):
    if not root:
        return

    def dfs(node, level):
        if not node:
            return

        if level % 2 == 1:
            print(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 1)

# Create the binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

# Define the nodes
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3, None, node6)
root = TreeNode(1, node2, node3)

# Call the function to print nodes at odd levels
print("Nodes at odd levels:")
print_nodes_at_odd_levels(root)
