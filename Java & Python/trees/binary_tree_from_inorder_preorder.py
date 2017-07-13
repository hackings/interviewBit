# traverse through preorder, find root_index
# left = inorder[:root_index], right = inorder[root_index+1:]
# root.left = preorder[1:left+1], left
# root.right = preorder[1left+1:], right

class Solution:
    # @param preorder : list of integers denoting preorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
    	if not inorder:
    		return None
    	root_val = preorder[0]
    	root_index = inorder.index(root_val)

    	left_nodes = inorder[:root_index]
    	right_nodes = inorder[root_index+1:]

    	left_len,right_len = len(left_nodes), len(right_nodes)
    	root = TreeNode(root_val)
    	root.left = self.buildTree(preorder[1:left_len+1], left_nodes)
    	root.right = self.buildTree(preorder[left_len+1:], right_nodes)

    	return root


"""
Given preorder and inorder traversal of a tree, construct the binary tree.

 Note: You may assume that duplicates do not exist in the tree. 
Example :

Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]

Return :
            1
           / \
          2   3
"""