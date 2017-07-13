# Concept correct, see Java version
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a double
	def findMedianSortedArrays(self, A, B):
		len_ = len(A)+len(B)
		if (len_ % 2 == 1):
			return self.findKth(A, 0, B, 0, len_/2+1)
		else:
			return ( self.findKth(A, 0, B, 0, len_/2) + self.findKth(A, 0, B, 0, len_/2 + 1) ) / 2.0

	def findKth(self, A, a, B, b, k):
		
		if a >= len(A):
			return B[b+k-1]
		if b >= len(B):
			A[a+k-1]
		if k == 1:
			return min(A[a], B[b])
		if a + k/2-1 < len(A):
			a_key =  A[a+k/2-1]
		else:
			a_key = sys.maxint
		if b + k/2-1 < len(B):
			b_key = B[b+k/2-1]
		else:
			b_key = sys.maxint

		if a_key < b_key:
			return self.findKth(A, a+k/2, B, b, k-k/2)
		else:
			return self.findKth(A, a+k/2, B, b+k/2, k-k/2)

"""
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
"""