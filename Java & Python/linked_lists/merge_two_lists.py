# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
		if not A:
			return B
		if not B:
			return A
		res = ListNode(0)
		p1, p2 = A, B
		root = res

		while p1 and p2:
			if p1.val < p2.val:
				res.next = p1
				p1 = p1.next
				res = res.next
			else:
				res.next = p2
				p2 = p2.next
				res = res.next
		if p1 is not None:
			res.next = p1
		elif p2 is not None:
			res.next = p2
		return root.next
"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
"""