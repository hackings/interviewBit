# Concept correct but taken from geeks for geeks
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a double
	def findMedianSortedArrays(self, A, B):
		if len(A) > len(B):			# A < B
			A,B = B,A
		self.findMedian(A, len(A), B, len(B))
	def findMedian(self, A, N, B, M):
		if len(A) == 0:
			return self.median_one_array(B)
		if len(A) == 1:
			if (len(B)) == 1:
				return self.median(A[0],B[0])
			if (len(B) % 2 == 1):			# odd
				a = B[M/2]
				b = self.median3(A[0], B[M/2-1], B[M/2+1])
				return self.median(a, b)
			# even
			return self.median3(B[M/2], B[M/2-1], A[0])
		elif len(A) == 2:
			if len(B) == 2:
				return self.median4(A[0], A[1], B[0], B[1])
			if len(B) % 2 == 1:
				a = B[M/2]
				b = max (A[0], B[M/2-1])
				c = min(A[1], B[M/2+1])
				return self.median3(a, b, c)
			# even
			a = B[M/2]
			b = B[M/2-1]
			c = max(A[0], B[M/2-2])
			d = min (A[1], B[M/2+1])
			return self.median4(a, b, c, d)
		index_a = (N-1) / 2
		index_b = (M-1) / 2

		if A[index_a] <= b[index_b]:
			# A[index_a ... n-1] and B[0 ... index_b]
			return self.findMedian(A + index_a, N/2+1, B, M-index_a)
		# A[0 .. index_a] and B[index_b ... n-1]
		return self.findMedian(A, N/2+1, B + index_a, M - index_a)

	def median_one_array(B):
		if len(B) % 2 == 0:
			return (B[len(B)/2] + B[len(B)/2-1]) / 2
		return B[len(B)/2]
	def median(a, b):
		return (a+b)/2.0
	def median3(a, b, c):
		return a + b + c - max(a, max(b,c)) - min(a, min(b,c))
	def median4(a, b, c, d):
		Max = max(a, max(b, max(c, d)))
		Min = min( a, min(b, min(c, d)))
		return (a + b + c + d - Max - Min) / 2.0
