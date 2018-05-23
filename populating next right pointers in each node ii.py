# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = root
        prev = TreeLinkNode(-1)
        curr = prev
        while head:
            while head:
                curr.next = head.left
                curr = curr.next or curr
                curr.next = head.right
                curr = curr.next or curr
                head = head.next
            head, curr = prev.next, prev
