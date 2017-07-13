# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
		return A == None or self.helper(A.left, A.right)
	def helper(self, left, right):
		if left is None or right is None:
			return left == right
		if left.val != right.val:
			return False

		return self.helper(left.left, right.right) and self.helper(left.right, right.left)

"""

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example :

	1
   / \
  2   2
 / \ / \
3  4 4  3
The above binary tree is symmetric. 
But the following is not:

	1
   / \
  2   2
   \   \
   3    3
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""