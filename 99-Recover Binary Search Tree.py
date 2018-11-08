# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.node1 = None
        self.node2 = None
        stack = []
        curr = root
        prev = None
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            
            if prev and prev.val > curr.val:
                if not self.node1:
                    self.node1 = prev
                if self.node1:
                    self.node2 = curr
            
            prev = curr
            curr = curr.right
            
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

            
