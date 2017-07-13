# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
		res, stack = [], []
		root = A
		while  len(stack) > 0 or root != None:
			if root != None:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()	# removes last val
				res.append(root.val)
				root = root.right
		return res
"""
Inorder TraversalBookmark
Given a binary tree, return the inorder traversal of its nodes’ values.

Example :
Given binary tree

   1
	\
	 2
	/
   3
return [1,3,2].

Using recursion is not allowed.
"""