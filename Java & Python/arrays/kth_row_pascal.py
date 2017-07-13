class Solution:
	# @param A : integer
	# @return a list of integers
	def getRow(self, A):
		A += 1
		res = [[1]]
		if A == 0:
			return res
		for i in xrange(2, A+1):
			res.append([0]*i)
			res[i-1][0] = 1 		# 1st item 1
			res[i-1][-1] = 1 		# last item 1
			for j in xrange(1, i-1):
				res[i-1][j] = res[i-2][j-1] + res[i-2][j]
		return res[-1]
"""
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
Note:Could you optimize your algorithm to use only O(k) extra space?


---

num at position i = number at position i in prev row + number at position (i + 1) in previous row.

Also, notice that for a row, you only need the value in the previous rows.

The values in i-2 row do not matter.

As such, all you need is to maintain 2 vectors and alternate between them.
"""