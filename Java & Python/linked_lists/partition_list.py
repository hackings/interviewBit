class Solution:
	# @param {ListNode} head
	# @param {integer} x
	# @return {ListNode}
	def partition(self, head, x):
		if not head:
			return None

		less, greaterEqual = ListNode(0), ListNode(0)
		tempLess, tempGreaterEqual = less, greaterEqual
		while head:
			if head.val < x:
				tempLess.next = head
				tempLess = tempLess.next
			else:
				tempGreaterEqual.next = head
				tempGreaterEqual = tempGreaterEqual.next

			cur = head
			head = head.next
			cur.next = None

		tempLess.next = greaterEqual.next
		return less.next

"""

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

Maintain 2 pointers - one which maintains all nodes less than x and another which maintains nodes greater than or equal to x. 
Keep going along our list. When we are at node that is greater than or equal to x, we remove this node from our list and move it to list of nodes greater than x.
"""