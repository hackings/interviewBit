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
    	if root is None:
    		return 0
    	left_max = self.maxDepth(root.left) + 1
    	right_max = self.maxDepth(root.right) + 1
    	return max(left_max, right_max)