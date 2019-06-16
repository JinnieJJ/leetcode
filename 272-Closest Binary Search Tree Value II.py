# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def dfs(root, target, heap):
            if not root:
                return 
            dfs(root.left, target, heap)
            heapq.heappush(heap, (abs(root.val - target), root.val))
            dfs(root.right, target, heap)
        
        heap = []
        dfs(root, target, heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
