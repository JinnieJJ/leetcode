"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        head = root
        prev = Node(-1)
        curr = prev
        while head:
            while head:
                curr.next = head.left
                curr = curr.next or curr
                curr.next = head.right
                curr = curr.next or curr
                head = head.next
            head, curr = prev.next, prev
        return root
