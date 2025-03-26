class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append('#')
        vals = []
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def preorder():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        vals = iter(data.split())
        return preorder()

# Example usage:
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

serialized_tree = codec.serialize(root)
print(serialized_tree)  # Output: 1 2 # # 3 4 # # 5 # #

deserialized_root = codec.deserialize(serialized_tree)
