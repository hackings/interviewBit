class Node:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.space = end-start
		self.left = None
		self.right = None
def build_tree(A):
	if A.end - A.start <= 1:
		return
	mid = (A.start + A.end) / 2
	A.left = Node(A.start, mid)
	A.right = Node(mid, A.end)
	build_tree(A.left)
	build_tree(A.right)

def find_pos(A, infront):
	A.space -= 1
	if A.left is None:
		return A.start
	if A.left.space > infront:
		return find_pos(A.left, infront)
	else:
		return find_pos(A.right, infront-A.left.space)
class Solution:
	# @param heights : list of integers
	# @param infronts : list of integers
	# @return a list of integers
	def order(self, heights, infronts):
		res = [0]*len(heights)
		root = Node(0, len(heights))
		build_tree(root)

		for (h, i) in sorted(zip(heights, infronts)):
			pos = find_pos(root, i)
			res[pos] = h
		return res
"""
You are given the following :

A positive number N
Heights : A list of heights of N persons standing in a queue
Infronts : A list of numbers corresponding to each person (P) that gives the number of persons who are taller than P and standing in front of P
You need to return list of actual order of persons’s height

Consider that heights will be unique

Example

Input : 
Heights: 5 3 2 6 1 4
InFronts: 0 1 2 0 3 2
Output : 
actual order is: 5 3 2 1 6 4 
So, you can see that for the person with height 5, there is no one taller than him who is in front of him, and hence Infronts has 0 for him.

For person with height 3, there is 1 person ( Height : 5 ) in front of him who is taller than him.

You can do similar inference for other people in the list.
"""