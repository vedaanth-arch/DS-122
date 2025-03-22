print("Binary Search Tree")
class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.data)+"->",end="")
        inorder(root.right)

    '''inserting from roo node where if the inserting node is greater
then it goes on right side and less than it goes to left side'''
def insert(root, data):
    '''Inserts a node in the binary search tree.'''
    if root is None:
        return BST(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def minval(root):
    if root is None:
        return None
    # Traverse to the leftmost node
    temp = root
    while temp.left is not None:
        temp = temp.left
    return temp

def maxval(root):
    if root is None:
        return None
    # Traverse to the rightmost node
    current = root
    while current.right is not None:
        current = current.right
    return current.data

def deleteNode(root, data):
    # Return if the tree is empty
    if root is None:
        return root
    # Find the node to be deleted
    if data < root.data:
        root.left = deleteNode(root.left, data)
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    else:
        # If the node has only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # If the node has two children, find the inorder successor
        temp = minval(root.right)
        root.data = temp.data
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)

    return root



        

    


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
print("Inorder traversal: ", end=' ')
inorder(root)
print()
min_value = minval(root)
max_value = maxval(root)
print("The minimum value in the tree is:", min_value if min_value is not None else "Tree is empty")
print("The maximum value in the tree is:", max_value if max_value is not None else "Tree is empty")
print("Inorder traversal: ", end=' ')
inorder(root)
print("\nDelete 10")
root = deleteNode(root, 8)
print("Inorder traversal: ", end=' ')
inorder(root)
