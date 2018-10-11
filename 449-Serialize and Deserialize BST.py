# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res, stack = [], []
        while stack or root:
            if root:
                res.append(str(root.val))
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return ' '.join(res)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = map(int, data.split(' '))
        stack = []
        root = node = TreeNode(data[0])
        for n in data[1:]:
            if n < node.val:
                node.left = TreeNode(n)
                stack.append(node)
                node = node.left
            else:
                while stack and stack[-1].val < n:
                    node = stack.pop()
                node.right = TreeNode(n)
                node = node.right
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
