# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.recursionHelper(root, sum, [], result)
        return result
    
    def recursionHelper(self, root, sum, cur, result):
        if not root:
            return
        sum -= root.val
        if sum == 0 and not root.left and not root.right:
            result.append(cur+[root.val])
        if root.left:
            self.recursionHelper(root.left, sum, cur+[root.val], result)
        if root.right:
            self.recursionHelper(root.right, sum, cur+[root.val], result)
