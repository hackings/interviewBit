# if A.val == A.next.val do another loop to see if it matches the current duplicate
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
		head = result = ListNode('dummy')

		while A:
			if A.next and A.val == A.next.val:
				duplicate = A.val
				while A and A.val == duplicate:
					A = A.next
			else:
				head.next = A
				head = head.next
				A = A.next
		head.next = None
		return result.next
"""
Remove Duplicates from Sorted List IIBookmark
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""