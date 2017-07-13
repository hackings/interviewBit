class BSTIterator:
	# @param root, a binary search tree's root node
	def __init__(self, root):
		self.root = root
		self.path = []
		A = root
		while A:
			self.path.append(A)
			A = A.left
	# @return a boolean, whether we have a next smallest number
	def hasNext(self):
		return len(self.path) != 0
	# return an integer, the next smallet number
	def next(self):
		res = self.path.pop()
		if res.right:
			A = res.right
			while A:
				self.path.append(A)
				A = A.left
		return res.val
"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST. Calling next() again will return the next smallest number in the BST, and so on.

 Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
Try to optimize the additional space complexity apart from the amortized time complexity. 
"""