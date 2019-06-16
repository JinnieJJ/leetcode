# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recursionHelper(node):
            if not node:
                return False
            left = recursionHelper(node.left)
            right = recursionHelper(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return node.val == 1 or left or right
        
        return root if recursionHelper(root) else None
