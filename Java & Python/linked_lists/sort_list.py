# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
    	if A is None or A.next is None:
    		return A
    	p1, p2 = A, A.next
    	# split list in half
    	while p2 and p2.next:
    		p1 = p1.next
    		p2 = p2.next.next
    	p2 = p1.next
    	p1.next = None
    	return self.mergeLists(self.sortList(A), self.sortList(p2))
    def mergeLists(self, l1, l2):
    	if l1 is None:
    		return l2
    	if l2 is None:
    		return l1
    	A = None
    	# setting the head
    	if l1.val < l2.val:
    		A = l1
    		l1 = l1.next
    	else:
    		A = l2
    		l2 = l2.next
    	root = A

    	while l1 and l2:
    		if l1.val < l2.val:
    			root.next = l1
    			l1 = l1.next
    		else:
    			root.next = l2
    			l2 = l2.next
    		root = root.next
    	# add the rest of the tail
    	if l1:
    		root.next = l1
    	else:
    		root.next = l2
    	return A
"""
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 2 -> 4 -> 5
"""