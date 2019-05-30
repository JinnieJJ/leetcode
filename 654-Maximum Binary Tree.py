# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.recursionHelper(nums, 0, len(nums))
    
    def recursionHelper(self, nums, l, r):
        if l == r:
            return None
        max_i = self.maxHelper(nums, l, r)
        root = TreeNode(nums[max_i])
        root.left = self.recursionHelper(nums, l, max_i)
        root.right = self.recursionHelper(nums, max_i+1, r)
        return root
    
    def maxHelper(self, nums, l, r):
        max_i = l
        for i in range(l, r):
            if nums[max_i] < nums[i]:
                max_i = i
        return max_i
        
