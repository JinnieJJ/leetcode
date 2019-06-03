# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        result = 0
        if root.left:
            result += self.distributeCoins(root.left)
            root.val += root.left.val - 1
            result += abs(root.left.val - 1)
        if root.right:
            result += self.distributeCoins(root.right)
            root.val += root.right.val - 1
            result += abs(root.right.val - 1)
            
        return result
        
