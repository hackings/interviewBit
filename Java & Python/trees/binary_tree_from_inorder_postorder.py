

class Solution:
	# @param inorder : list of integers denoting inorder traversal
	# @param postorder : list of integers denoting postorder traversal
	# @return the root node in the tree
	def buildTree(self, inorder, postorder):
		if not inorder or not postorder:
			return None
		
		root = TreeNode(postorder.pop())
		root_index = inorder.index(root.val)
		
		leftNodes = inorder[:root_index]
		rightNodes = inorder[root_index+1:]

		# order matters [left children -> right children], right goes first
		root.right = self.buildTree(rightNodes, postorder)
		root.left = self.buildTree(leftNodes, postorder)
		
		return root