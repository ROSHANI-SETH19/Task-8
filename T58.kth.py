class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    # This helper function will perform an in-order traversal
    def in_order_traversal(node):
        if node is None:
            return []
        # Traverse left, then root, then right
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    # Perform in-order traversal and return the k-th smallest element
    in_order_result = in_order_traversal(root)
    return in_order_result[k - 1]  # K-th smallest, 1-based index

# Example usage:
# Creating a simple BST:
#       5
#      / \
#     3   6
#    / \
#   2   4
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

k = 3
print(kthSmallest(root, k))  # Output should be 4 (3rd smallest element)
