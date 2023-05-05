from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    max_sum = float('-inf')  # Initialize with negative infinity
    level = 1

    while queue:
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum

        level += 1

    return max_sum



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

# Call the function to find the maximum level sum
max_sum = max_level_sum(root)

# Print the result
print("Maximum level sum:", max_sum)
