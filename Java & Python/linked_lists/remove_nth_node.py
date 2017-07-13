# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
    	if A is None:
    		return A
    	p1, p2 = A, A
    	for i in xrange(B):
    		if p2 is None:
    			p2 = p2
    		else:
    			p2 = p2.next
    	if p2 is None:
    		return A.next
    	prev = None
    	while p2 != None:
    		p2 = p2.next
    		prev = p1
    		p1 = p1.next
    	prev.next = p1.next

    	return A


"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

 Note:
* If n is greater than the size of the list, remove the first node of the list. 
Try doing it using constant additional space.


1 - 2 - 3 - 4 - 5
p1      p2
prev p1      p2
   prev p1      p2
      prev  p1      p2

      prev.next = p1.next
"""