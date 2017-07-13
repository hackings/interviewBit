# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : tuple of integers
	# @return the root node in the tree
	def sortedArrayToBST(self, A):
		mid = (len(A)-1)/2
		root = TreeNode(A[mid])

		if A[:mid]:
			root.left = self.sortedArrayToBST(A[:mid])
		if A[mid+1:]:
			root.right = self.sortedArrayToBST(A[mid+1:])

		return root


"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

 Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Example :


Given A : [1, 2, 3]
A height balanced BST  : 

	  2
	/   \
   1     3

"""
