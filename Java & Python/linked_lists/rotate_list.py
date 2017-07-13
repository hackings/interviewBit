# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def rotateRight(self, A, B):
		if A is None:
			return None
		temp = A
		for i in xrange(B):
			if temp.next == None:
				temp = A
			else:
				temp = temp.next
		last = A
		while temp.next != None:
			temp = temp.next
			last = last.next
		temp.next = A
		res = last.next
		last.next = None
		return res
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""