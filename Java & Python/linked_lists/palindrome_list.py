# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
		head = A
		p1, p2 = self.findMidandReverse(head)
		while p1 and p2:
			if p1.val == p2.val:
				p1 = p1.next
				p2 = p2.next
			else:
				return 0
		return 1

	def findMidandReverse(self,A):
			if A is None or A.next is None:
				return A, A
			p1, p2 = A, A

			while p1 and p2:
				p2 = p2.next
				if p2:
					p2 = p2.next
				prev = p1
				p1 = p1.next
			
			##Found Mid now reversing
			prev = p1
			curr = p1.next
			while curr:
				curr.next , prev,  curr = prev, curr, curr.next		# doing this on 3 sep lines doesn't work
			
			p1.next = None
			return A, prev


"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes: 
- Expected solution is linear in time and constant in space.

For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""