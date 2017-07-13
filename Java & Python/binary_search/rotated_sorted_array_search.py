# find the min, do binary search from [0..min] and [min..len(A)-1]]
# when finding min, A[mid]<A[end] and A[mid] > A[end]
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def search(self, A, target):
		if A is None:
			return None
		index = self.findMin(A, 0, len(A)-1)
		# 0 - index
		index1 = self.binarySearch(A, 0, index, target)
		if index1 != -1:
			return index1
		# index - len(A)-1
		return self.binarySearch(A, index, len(A)-1, target)

	def findMin(self, A, start, end):
		if start > end:
			return -1
		if start == end:
			return start
		mid = (start + end)/2
		if A[mid] < A[end]:
			return self.findMin(A, start, mid)
		elif A[mid] > A[end]:
			return self.findMin(A, mid+1, end)
	
	def binarySearch(self, A, start, end, target):
		if start > end: return -1
		if start == end:
			if A[start] == target:
				return start
			return -1
		mid = (start+end)/2
		if A[mid] < target:
			return self.binarySearch(A, mid+1, end, target)
		else:
			return self.binarySearch(A, start, mid, target)
		

"""

0 1 2 3 4 5 6 7

4 5 6 7 0 1 2

there should be a point in time where the  [i-1] > [i]

low = 0
high = len(A)-1
i is the pivot = (0 + len(A))/2



Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
"""