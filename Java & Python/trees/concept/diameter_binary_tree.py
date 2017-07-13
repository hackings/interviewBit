def diameter_binary_tree(self, A, height):

	if A is None:
		height = 0
		return 0

	left_height = self.height(A.left)
	right_height = self.height(A.right)

	left_diameter = self.diameter_binary_tree(A.left, left_height)
	right_diameter = self.diameter_binary_tree(A.right, right_height)

	height = max(left, right) + 1		# height of current node

	return max(left_height+right_height+1, left_diameter, right_diameter)

def height(self, A):
	if root is not None:
		return max(self.height(A.left), self.height(A.right)) + 1
	return 0
"""
Find diameter of binary tree
remember, could be through the root or not through the root

O(N)
"""
