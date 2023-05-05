from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_preorder(root):
    if root is None:
        return

    print(root.value)
    dfs_preorder(root.left)
    dfs_preorder(root.right)

def dfs_inorder(root):
    if root is None:
        return

    dfs_inorder(root.left)
    print(root.value)
    dfs_inorder(root.right)

def dfs_postorder(root):
    if root is None:
        return

    dfs_postorder(root.left)
    dfs_postorder(root.right)
    print(root.value)


# Example usage:
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("BFS:")
bfs(root)

print("DFS (Preorder):")
dfs_preorder(root)

print("DFS (Inorder):")
dfs_inorder(root)

print("DFS (Postorder):")
dfs_postorder(root)
