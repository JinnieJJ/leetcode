# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = 0, 0
        while l1:
            s1 *= 10
            s1 += l1.val
            l1 = l1.next
        while l2: 
            s2 *= 10
            s2 += l2.val
            l2 = l2.next
            
        s3 = s1 + s2
        head = None
        while s3 > 0 :
            node = ListNode(s3 % 10)
            node.next, head = head, node
            s3 //= 10
        return head if head else ListNode(0)
