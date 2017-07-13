import operator

class Solution:
	def buildTree(self, values):
		if not values:
			return None
		max_index, max_value = max(enumerate(values), key=operator.itemgetter(1))
		
		root = TreeNode(max_value)
		root.left = self.buildTree(values[:max_index])
		root.right = self.buildTree(values[max_index+1:])

		return root
"""

Given an inorder traversal of a cartesian tree, construct the tree.

 Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree. 
 Note: You may assume that duplicates do not exist in the tree. 
Example :

Input : [1 2 3]

Return :   
		  3
		 /
		2
	   /
	  1
"""