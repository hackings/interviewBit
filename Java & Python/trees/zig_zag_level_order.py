# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
    	self.levels = []
    	self.traverse(A, 1)

    	for i, level in enumerate(self.levels):
    		if i % 2 == 0:
    			self.levels[i] = level[::-1]
    	return self.levels

    def traverse(self, A, level):
    	if A is None:
    		return

    	self.traverse(A.right, level+1)
    	self.traverse(A.left, level+1)

    	self.updateLevel(A, level)

    def updateLevel(self, A, level):
    	while len(self.levels) < level:
    		self.levels.append([])
    	self.levels[level-1].append(A.val)		# level started at 1

"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. (ie, from left to right, then right to left for the next level and alternate between).

Example : 
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return

[
         [3],
         [20, 9],
         [15, 7]
]
"""