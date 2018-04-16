# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result.next = head
        tmp = result
        while tmp.next and tmp.next.next:
            node1 = tmp.next
            node2 = tmp.next.next
            node3 = tmp.next.next.next
            tmp.next = node2
            node2.next = node1
            node1.next = node3
            tmp = node1
        return result.next
