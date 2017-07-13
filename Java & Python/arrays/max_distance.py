class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maximumGap(self, A):
		res = -1
		right_max, left_min = [0]*len(A), [0]*len(A)
		left_min[0] = A[0]
		right_max[len(A)-1] = A[len(A)-1]

		for i in xrange(1, len(A)):
			left_min[i] = min(left_min[i-1], A[i])
		for i in xrange(len(A)-2, -1, -1):
			right_max[i] = max(right_max[i+1], A[i])

		i = j = 0
		while i < len(A) and j < len(A):
			if left_min[i] <= right_max[j]:
				res = max(res, j-i)
				j += 1
			else:
				i += 1
		return res



"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)
"""