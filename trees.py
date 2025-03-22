class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_path(root, path, target):
    # Base case: if the root is None, return False
    if root is None:
        return False

    # Add the current node to the path
    path.append(root.value)

    # Check if the current node is the target node
    if root.value == target:
        return True

    # Recursively check in the left and right subtrees
    if (root.left and find_path(root.left, path, target)) or \
       (root.right and find_path(root.right, path, target)):
        return True

    # If the target is not present in either subtree, remove the current node from the path
    path.pop()
    return False

def print_path(root, target):
    path = []
    if find_path(root, path, target):
        print("Path from root to node", target, ":", " -> ".join(map(str, path)))
    else:
        print("Node", target, "not found in the tree.")

# Example usage:
# Constructing the binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Print path from root to a specific node
print_path(root, 5)  # Expected output: Path from root to node 5 : 1 -> 2 -> 5
print_path(root, 3)  # Expected output: Path from root to node 3 : 1 -> 3
print_path(root, 6)  # Expected output: Node 6 not found in the tree.
