# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the first node in the cycle in the linked list
	def detectCycle(self, root):
		if not root or not root.next:
			return None
		isCycle = False
		p2, p1 = root, root
		while p1 and p2:
			p1 = p1.next
			if p2.next == None:
				return None
			p2 = p2.next.next
			if p1 == p2:
				isCycle = True
				break
		if isCycle is False:
			return None
		p1 = root
		while p1 != p2:
			p1 = p1.next
			p2 = p2.next
		return p1
"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 
"""