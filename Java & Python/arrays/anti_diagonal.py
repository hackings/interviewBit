class Solution:
	# @param A : list of list of integers
	# @return a list of list of integers
	def diagonal(self, A):
		p = len(A[0])
		res = [0]*(2*p-1)		# 3x3 matrix = 5 anti diagonals
		for i in xrange(2*p-1):
			res[i] = []
		for i in xrange(p):
			for j in xrange(p):
				res[i+j].append(A[i][j])
		return res
"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

		
Input: 	

1 2 3
4 5 6
7 8 9

Return the following :

[ 
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]


Input : 
1 2
3 4

Return the following  : 

[
  [1],
  [2, 3],
  [4]
]

"""