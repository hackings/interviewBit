# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, A, B):
		if not B:
			return A
		if not A:
			return B

		head = res = ListNode('dummy')
		carry = 0
		while A or B or carry:
			a_val = 0 if A is None else A.val
			b_val = 0 if B is None else B.val
			
			total = a_val + b_val + carry 
			val = total % 10
			res.next = ListNode(val)
			res = res.next
			carry = total / 10
			if A:
				A = A.next
			if B:
				B = B.next
		return head.next
"""

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

3 1 + 9

item to put in linked list 12 % 10 = 2
carry = 12 / 10

13 + 9 = 2


899
238
  7

carry starts out as 0
8 + 9 = 17
17 % 10 = 7
carry 17 / 10 = 1

(9 +  3 + carry)%10 = item 
"""