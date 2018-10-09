"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def traverse(node):
            if not node.left and not node.right:
		        return node, node
            
            if node.left:
                hl, tl = traverse(node.left)
                tl.right = node
                node.left = tl      
            else:
                hl, tl = node, node
            
            if node.right:
                hr, tr = traverse(node.right)
                hr.left = node
                node.right = hr   
            else:
                hr, tr = node, node
            
            return hl, tr
        
        if not root:
            return None
        hl, tr = traverse(root)
        hl.left = tr
        tr.right = hl
        
        return hl
