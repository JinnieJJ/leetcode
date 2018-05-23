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
        return self.Recursion(root, 0)

    def Recursion(self, root, s):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return s * 10 + root.val

        return self.Recursion(root.left, s * 10 + root.val) + self.Recursion(root.right, s * 10 + root.val)
