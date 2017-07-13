class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generate(self, A):
		res = []
		curr = 0
		if A == 0:
			return res
		res = [[1]]
		for i in xrange(2, A+1):
			 res.append([0]*i)
			 res[i-1][0] = 1 	# first
			 res[i-1][-1] = 1 	# last
			 for j in xrange(1, i-1):
			 	res[i-1][j] = res[i-2][j-1] + res[i-2][j]
		return res


"""
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""