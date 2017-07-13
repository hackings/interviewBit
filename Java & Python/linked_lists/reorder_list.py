# even node.next = a[i/2]
# odd node.next = a[length-1-i]

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reorderList(self, root):
		a, A, length = [], root, 0
		while A:
			a.append(A)
			length += 1
			A = A.next
		node = a[0]
		for i in xrange(1, length):
			if i % 2 == 0:
				node.next = a[i/2]
				node = node.next
				if i == length-1:		# last one
					node.next = None
			else:
				node.next = a[length-1 - i/2]
				node = node.next
				if i == length-1:		# last one
					node.next = None
		return root



"""

Given a singly linked list

	L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

	L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""