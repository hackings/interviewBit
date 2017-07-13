# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, root):
		if (not self.validBST(root, float('-inf'), float('inf'))):
			return 0
		else:
			return 1
	def validBST(self, root, low, high):
		if root is None:
			return True
		
		return (low < root.val < high and 
				self.validBST(root.left, low, root.val) and
				self.validBST(root.right, root.val, high))