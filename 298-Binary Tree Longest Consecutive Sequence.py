# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [(root, 1)]
        maxlen = 1
        while stack:
            e = stack.pop()
            if e[0].left:
                if e[0].left.val == e[0].val + 1:
                    stack.append((e[0].left, e[1]+1))
                    maxlen = max(maxlen, e[1]+1)
                else:
                    stack.append((e[0].left, 1))
            if e[0].right:
                if e[0].right.val == e[0].val + 1:
                    stack.append((e[0].right, e[1]+1))
                    maxlen = max(maxlen, e[1]+1)
                else:
                    stack.append((e[0].right, 1))
        return maxlen
