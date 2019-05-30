# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum
    
    def max_gain(self, node):
        if not node:
            return 0
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)
        price_newpath = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, price_newpath)
        return node.val + max(left_gain, right_gain)
    
