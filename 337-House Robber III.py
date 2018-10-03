# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return(0, 0)
            left, right = helper(root.left), helper(root.right)
            rob = root.val + left[1] + right[1]
            notrob = max(left) + max(right)
            return (rob, notrob)
        
        return max(helper(root))
