# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0 # number of nodes
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        for i in range(count - ( k % count )): # find the position of head
            p = p.next
        dummy.next = p.next # position of head: p.next
        p.next = None # position of tail: p
        return dummy.next
