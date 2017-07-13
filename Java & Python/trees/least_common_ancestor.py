# make 2 arrays of the path to each root
# compare arrays, they'll be the same numbers until the path differs
# break out when path differs, last num was lowest ancestor
class Solution:
	# @param root : root node of tree
	# @param val1 : integer
	# @param val2 : integer
	# @return an integer
	def lca(self, root, val1, val2):
		s1, s2 = [], []

		if self.path(root, s1, val1) == False or self.path(root, s2, val2) == False:
			return -1
		i = 0
		while i < len(s1) and i < len(s2):
			if s1[i] != s2[i]:
				break
			i += 1
		return s1[i-1]
	def path(self, root, s, val):
		if root == None:
			return False
		s.append(root.val)
		if root.val == val:
			return True
		if (root.left != None and self.path(root.left,s,val) or (root.right != None and self.path(root.right,s,val))):
			return True
		s.pop()
		return False
"""
Find the lowest common ancestor in an unordered binary tree given two values in the tree.

 Lowest common ancestor : the lowest common ancestor (LCA) of two nodes v and w in a tree or directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants. 
Example :


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2_     0        8
         /   \
         7    4
For the above tree, the LCA of nodes 5 and 1 is 3.

 LCA = Lowest common ancestor 
Please note that LCA for nodes 5 and 4 is 5.

You are given 2 values. Find the lowest common ancestor of the two nodes represented by val1 and val2
No guarantee that val1 and val2 exist in the tree. If one value doesn’t exist in the tree then return -1.
There are no duplicate values.
You can use extra memory, helper functions, and can modify the node struct but, you can’t add a parent pointer.
"""