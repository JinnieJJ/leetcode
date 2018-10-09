# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, i = queue.popleft()
            if node:
                cols[i].append(node.val)
                queue.append((node.left, i-1))
                queue.append((node.right, i+1))
        return [cols[i] for i in range(min(cols.keys()), max(cols.keys()) + 1)] if cols else []
        
