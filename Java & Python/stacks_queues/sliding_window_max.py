from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
		queue = deque()
		ret = []
		n = len(A)
		
		for i in range(B):
			while len(queue) != 0 and i < n and A[i] >= A[queue[-1]]:
				queue.pop()
			queue.append(i)
		for i in range(B,n):
			ret.append(A[queue[0]])
			while len(queue) != 0 and A[i] >= A[queue[-1]]:
				queue.pop()
			while len(queue) != 0 and queue[0] <= i-B:
				queue.popleft()
			queue.append(i)
		ret.append(A[queue[0]])
		return ret

"""
A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position.

Example :

The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position	Max
 	 
[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]

 Note: If w > length of the array, return 1 element with the max of the array. 

 """