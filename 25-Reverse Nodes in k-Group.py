# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        if k <= 1 or length < k:
            return head
        
        pre = None
        cur = head
        for _ in range(k):
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        head.next = self.reverseKGroup(cur, k)
        return pre

