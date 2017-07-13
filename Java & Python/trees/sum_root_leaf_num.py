# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def sumNumbers(self, A):
		return self.sumNum(A, 0)
	def sumNum(self, A, currentSum):
		if A is None:
			return currentSum
		currentSum = (currentSum * 10 + A.val) % 1003
		
		if A.left is None and A.right is None:
			return currentSum
		if A.left is None:
			return self.sumNum(A.right, currentSum)
		if A.right is None:
			return self.sumNum(A.left, currentSum)
		return (self.sumNum(A.left, currentSum) + self.sumNum(A.right, currentSum)) % 1003
"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
"""