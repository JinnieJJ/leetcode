# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        freq = collections.defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                freq[node.val] += 1
                return node.val
            val = node.val + dfs(node.left) + dfs(node.right)
            freq[val] += 1
            return val
        
        dfs(root)
        sorted_freq = sorted(freq.items(), key=lambda p:p[1], reverse=True)
        return [k for k,v in sorted_freq if v == sorted_freq[0][1]]
