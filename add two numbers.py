# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = None
        tmp = None
        while l1 is not None or l2 is not None or carry == 1:
            value = 0
            if l1 is not None:
                value += l1.val
                l1 = l1.next
            if l2 is not None:
                value += l2.val
                l2 = l2.next
            value += carry
            carry = int(value / 10)
            digit = int(value % 10)
            if result == None:
                result = ListNode(digit)
                tmp = result
            else:
                tmp.next = ListNode(digit)
                tmp = tmp.next
        return result
