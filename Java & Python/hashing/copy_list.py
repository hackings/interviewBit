# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
	def copyRandomList(self, root):
		d = dict()
		A = root
		_A, _root = None, None

		while A:
			_A = RandomListNode(A.label)
			if _root == None:
				_root = _A
			d[A] = _A
			A = A.next
		for key, val in d.iteritems():
			_A = val
			if key.next != None:
				_A.next = d[key.next]
			if key.random != None:
				_A.random = d[key.random]

		return _root

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or NULL.

Return a deep copy of the list.

Example

Given list

   1 -> 2 -> 3
with random pointers going from

  1 -> 3
  2 -> 1
  3 -> 1
You should return a deep copy of the list. The returned answer should not contain the same node as the original list, but a copy of them. The pointers in the returned list should not link to any node in the original input list.
"""