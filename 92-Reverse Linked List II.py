# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        for _ in range(m - 1):
            node = node.next
        pre = node.next
        cur = pre.next
        
        for _ in range(n - m):
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        node.next.next = cur
        node.next = pre
        return dummy.next
