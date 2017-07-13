# Always switching ij = ji
# ji = ij
class Solution:
	# @param A : list of list of integers
	# @return the same list modified
	def rotate(self, A):
		for i in xrange(len(A)/2):
			for j in xrange(i, len(A)-1-i):
				temp = A[i][j]									# 00
				A[i][j] = A[len(A)-1-j][i]						# 20
				A[len(A)-1-j][i] = A[len(A)-i-1][len(A)-j-1]	# 22
				A[len(A)-1-i][len(A)-j-1] = A[j][len(A)-i-1]	# 20
				A[j][len(A)-1-i] = temp							# 00
		return A
"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
"""