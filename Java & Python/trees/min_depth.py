# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def minDepth(self, root):
		if root is None:
			return 0
		if root.right is None and root.left is None:
			return 1
		if root.right is None:
			return 1 + self.minDepth(root.left)
		if root.left is None:
			return 1 + self.minDepth(root.right)
		return min(self.minDepth(root.left), self.minDepth(root.right)) + 1