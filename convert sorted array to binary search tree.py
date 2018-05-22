# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.Recursion(nums, 0, len(nums))

    def Recursion(self, nums, left, right):
        if left == right:
            return None
        mid = (left + right)//2
        root = TreeNode(nums[mid])
        root.left = self.Recursion(nums, left, mid)
        root.right = self.Recursion(nums, mid + 1, right)
        return root
