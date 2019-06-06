# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        self.recursionHelper(root)
        return self.count
        
    def recursionHelper(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True
        
        retval = True
        
        if node.left:
            retval = self.recursionHelper(node.left) and retval and node.left.val == node.val
        if node.right:
            retval = self.recursionHelper(node.right) and retval and node.right.val == node.val
        if retval:
            self.count += 1
        return retval
