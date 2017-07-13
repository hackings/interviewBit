
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
		res = []
		stack = []
		if A is None:
			return res
		stack.append(A)
		while len(stack):
			node = stack.pop(0)
			res.append(node.val)
			if node.right != None:
				stack.insert(0,node.right)
			if node.left != None:
				stack.insert(0,node.left)
			
		return res

