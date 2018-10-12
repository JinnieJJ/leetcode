# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res = 0
        queue = deque([(root, [])])
        while queue:
            node, prev = queue.popleft()
            if node:
                tmp = [node.val + p for p in prev] + [node.val]
                res += sum([v == target for v in tmp])
                queue.extend([(node.left, tmp), (node.right, tmp)])
        return res
