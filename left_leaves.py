class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_left_leaves(root):
    if not root:
        return 0
    
    # initialize the sum to 0
    left_sum = 0
    
    # traverse the left subtree
    if root.left:
        # if the left child is a leaf, add its value to the sum
        if not root.left.left and not root.left.right:
            left_sum += root.left.val
        # if the left child is not a leaf, recursively traverse its subtree
        else:
            left_sum += sum_left_leaves(root.left)
    
    # traverse the right subtree
    if root.right:
        # if the right child is not a leaf, recursively traverse its subtree
        if root.right.left or root.right.right:
            left_sum += sum_left_leaves(root.right)
    
    return left_sum
# create a binary tree
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

# find the sum of all left leaves
sum = sum_left_leaves(root)

# print the result
print(sum)  # output: 24
