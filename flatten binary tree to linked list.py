# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        while root:
            if root.left:
                if root.right:
                    stack.append(root.right)
                root.right, root.left = root.left, None
            if not root.right and stack:
                root.right = stack.pop()
            root = root.right
