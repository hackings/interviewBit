# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root : root node of tree
	# @param k : integer
	# @return an integer
	def kthsmallest(self, A, k):
		for val in self.inorder(A):
			if k == 1:		# k starting at 1 not 0
				return val
			else:
				k -= 1
	def inorder(self, A):
		if A:
			for val in self.inorder(A.left):
				yield val						# return generator
			yield A.val
			for val in self.inorder(A.right):
				yield val

"""
Given a binary search tree, write a function to find the kth smallest element in the tree.

Example :

Input : 
  2
 / \
1   3

and k = 2

Return : 2

As 2 is the second smallest element in the tree.
"""