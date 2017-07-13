class Solution:
	# @param A : list of list of integers
	# @return the same list modified
	def setZeroes(self, A):
		rowFlag, colFlag = False, False
		row, col = len(A), len(A[0])
		if row == 0 or col == 0:
			return A

		for i in xrange(col):	# first row = 0
			if A[0][i] == 0:
				rowFlag = True
				break
		for i in xrange(row):	# first col = 0
			if A[i][0] == 0:
				colFlag = True
				break
		# find the zeroes and store the info in first row and first column
		for i in xrange(1, row):
			for j in xrange(1, col):
				if A[i][j] == 0:
					A[0][j] = 0 		# first row
					A[i][0] = 0 		# first column

		for i in xrange(1, row):		# MEAT
			for j in xrange(1, col):
				if A[0][j] == 0 or A[i][0] == 0:
					A[i][j] = 0

		if rowFlag:
			for i in xrange(col):
				A[0][i] = 0
		if colFlag:
			for i in xrange(row):
				A[i][0] = 0
		return A



"""
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1
On returning, the array A should be :

0 0 0
1 0 1
1 0 1
Note that this will be evaluated on the extra memory used. Try to minimize the space and time complexity.
"""