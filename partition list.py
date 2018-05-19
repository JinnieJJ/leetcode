# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummySmall = ListNode(0)
        dummyBig = ListNode(0)
        Small = dummySmall
        Big = dummyBig
        while head:
            if head.val < x:
                Small.next = head
                Small = Small.next
            else:
                Big.next = head
                Big = Big.next
            head = head.next
        
        Small.next = dummyBig.next
        Big.next = None

        return dummySmall.next
