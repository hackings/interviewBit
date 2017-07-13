# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, root):
    	count = 0
    	if root is None:
    		return 0
    	elif root.left is None and root.right is None:
    		return 1
    	elif root.left is None:
    		return self.maxDepth(root.right)+1
    	elif root.right is None:
    		return self.maxDepth(root.left)+1
    	else:
    		return max(self.maxDepth(root.left), self.maxDepth(root.right))+1