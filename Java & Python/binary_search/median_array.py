class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a double
	def findMedianSortedArrays(self, A, B):
		if len(A) > len(B):		# B must be the larger list
			A,B = B,A
		m,n = len(A), len(B)
		low = 0
		high = m
		while low <= high:
			i = (low + high) / 2
			j = (m + n + 1) / 2 - i
			if j > 0 and i < m and B[j-1] > A[i]:
				low = i + 1 		# getting rid of lower half
			elif i > 0 and j < n and A[i-1] > B[j]:
				high = i-1			# getting rid of top half
			# figure out median now
			else:
				med1, med2 = 0,0
				if i == 0:
					med1 = B[j-1]
				elif j == 0:
					med1 = A[i-1]
				else:
					med1 = max(A[i-1], B[j-1])

				if (m+n) % 2 == 1:
					return 1.0 * med1
				if i == m:
					med2 = B[j]
				elif j == n:
					med2 = A[i]
				else:
					med2 = min(A[i], B[j])
				return (med1 + med2)/2.0
		return -1



"""

There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
 NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. 
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5 
"""