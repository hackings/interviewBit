
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def t2Sum(self, A, B):
		if not A:
			return False
		p1, p2, s1, s2 = A, A, [], []
		done1, done2 = False, False
		while True:
			while not done1:	#inorder 1
				if p1:
					s1.append(p1)
					p1 = p1.left
				else:
					if not s1:
						done1 = True
						continue
					p1 = s1.pop()
					val1 = p1.val
					p1 = p1.right
					done1 = True
			while not done2:	#inorder 2
				if p2:
					s2.append(p2)
					p2 = p2.right
				else:
					if not s2:
						done2 = True
						continue
					p2 = s2.pop()
					val2 = p2.val
					p2 = p2.left
					done2 = True
			if val1 >= val2:
				return 0
			
			if val1 + val2 == B and val1 != val2:
				return 1
			
			if val1 + val2 < B:
				done1 = False
			elif val1 + val2 > B:
				done2 = False


"""
Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.

Return 1 to denote that two such nodes exist. Return 0, otherwise.

Notes 
- Your solution should run in linear time and not take memory more than O(height of T).
- Assume all values in BST are distinct.

Example :

Input 1: 

T :       10
		 / \
		9   20

K = 19

Return: 1

Input 2: 

T:        10
		 / \
		9   20

K = 40

Return: 0

-------------------
If you do inorder traversal of BST you visit elements in increasing order. So, we use a two pointer approach, where we keep two pointers pt1 and pt2. Initially pt1 is at smallest value and pt2 at largest value.

Then we compare sum = pt1.value + pt2.value. If sum < target, we increase pt1, else we decrease pt2 until we reach target.
"""