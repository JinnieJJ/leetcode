# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # mergesort
        if head == None or head.next == None:
    		return head
    	fast = head
    	slow = head
    	while fast.next and fast.next.next:
    		fast = fast.next.next
    		slow = slow.next
    	head1 = head
    	head2 = slow.next
    	slow.next = None
    	head1 = self.sortList(head1)
    	head2 = self.sortList(head2)
    	return self.merge(head1, head2)
 
    #Merge
    def merge(self, head1, head2):
    	if not head1: 
            return head2
    	if not head2: 
            return head1
    	head = ListNode(-1)
    	pre = head
    	while head1 and head2:
    		if head1.val < head2.val:
    			pre.next = head1
    			head1 = head1.next
    		else:
    			pre.next = head2
    			head2 = head2.next
    		pre = pre.next
    	if not head1:
    		pre.next = head2
    	if not head2:
    		pre.next = head1
    	return head.next
