# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.recursionHelper(root, 0)
    
    def recursionHelper(self, root, s):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return s*10 + root.val
        
        return self.recursionHelper(root.left, s*10+root.val) + self.recursionHelper(root.right, s*10+root.val)
