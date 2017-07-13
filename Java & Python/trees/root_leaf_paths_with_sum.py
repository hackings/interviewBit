# see path_sum.py for more intuitive answer

class Solution:
		# @param root : root node of tree
		# @param sum1 : integer
		# @return a list of list of integers
		def pathSum(self, root, sum1):
			self.paths = []
			if A.left is not None:
				self.checkPath(A.left, sum1, A.val, [A.val])
			if A.right is not None:
				self.checkPath(A.right, sum1, A.val, [A.val])
			return self.paths
			
		def checkPath(self, node, sum1, current, path):
			if sum1 == node.val + current and if node.left is None and node.right is None:
				self.paths.append(path + [node.val])
				return
				
			if node.left is not None:
				self.checkPath(node.left, sum1, current + node.val, path + [node.val])
			if node.right is not None:
				self.checkPath(node.right, sum1, current + node.val, path + [node.val])

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

							5
						 / \
						4   8
					 /   / \
					11  13  4
				 /  \    / \
				7    2  5   1
return

[
	 [5,4,11,2],
	 [5,8,4,5]
]

22-5 = 17
17-4 = 13
13-11 = 2
2-2 = 0
"""