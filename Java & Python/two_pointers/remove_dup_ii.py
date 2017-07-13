# one pointer throughout entire array, 
# only increase 2nd pointer when you don't see A[i] == A[i+1] and A[i+2]
class Solution:
	# @param A : list of integers
	# @return an integer
	def removeDuplicates(self, A):
		count = 0
		for i in xrange(len(A)):
			if i < len(A)-2 and A[i] == A[i+1] and A[i] == A[i+2]:
				continue
			else:
				A[count] = A[i]
				count += 1
		A = A[:count]
		return count
"""
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].

 0  1  2  3  4  5  6
[2, 4, 6, 6, 6, 7, 7]
count = 2
i = 2
i = 3
A[2] = 6
count = 3
i = 4
A[3] = 6
count = 4
A[4] = 7
A[5] = 7
"""