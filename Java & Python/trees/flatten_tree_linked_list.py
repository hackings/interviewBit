# if root.left, go down to its right most child (Node X)
# attach everything from the right side to Node X
# shift root.left over to root.right

class Solution:
	# @param A : root node of tree
	# @return the root node in the tree
	def flatten(self, A):
		node = root = A
		while root:
			if root.left:
				prev = root.left
				while prev.right:
					prev = prev.right
				prev.right = root.right
				root.right = root.left
				root.left = None
			root = root.right
		return node

"""
Flatten Binary Tree to Linked ListBookmark
Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
"""