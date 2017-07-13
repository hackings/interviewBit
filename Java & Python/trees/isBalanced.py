# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	balanced = 1					# default to true
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
		self.findDepth(A)
		return self.balanced
	def findDepth(self, A):
		if A is None:
			return 0

		leftHeight = self.findDepth(A.left)+1
		rightHeight = self.findDepth(A.right)+1

		if abs(leftHeight - rightHeight) > 1:
			self.balanced = 0		# false

		return max(leftHeight, rightHeight)

"""
Given a binary tree, determine if it is height-balanced.

 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Example :

Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
"""