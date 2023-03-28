# Determine whether a tree is a Binary Search Tree or not

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst_recursive(node, lower=float('-inf'), upper=float('inf')):
    if node is None:
        return True
    if node.val <= lower or node.val >= upper:
        return False
    return is_valid_bst_recursive(node.left, lower, node.val) and is_valid_bst_recursive(node.right, node.val, upper)

Example 1
    root = Node(5)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(10)
    print(is_valid_bst_recursive(root))

Example 2
    root2 = Node(5)
    root2.left = Node(3)
    root2.right = Node(8)
    root2.left.left = Node(1)
    root2.left.right = Node(6)  
    root2.right.left = Node(6)  
    root2.right.right = Node(10)
    print(is_valid_bst_recursive(root2))
