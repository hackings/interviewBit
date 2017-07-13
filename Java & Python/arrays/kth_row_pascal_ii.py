class Solution:
	# @param A : integer
	# @return a list of integers
	def getRow(self, A):
		res = [[1]*2]
		if A < 0:
			return None
		numRows, currentRow, prevRow = A+1, 0, 1
	
		for i in xrange(1, numRows):
			currentRow, prevRow = prevRow, currentRow
			self.insert(res[currentRow], 0, 1)							# first item

			for j in xrange(0, len(res[prevRow])-1):					# in between
				self.insert(res[currentRow], j+1, res[prevRow][j] + res[prevRow][j+1])
			self.insert(res[currentRow], len(res[prevRow])-1, 1)		# last item
		return res[currentRow]

	def insert(res, index, val):
		if index >= len(res):
			res.append(val)
		else:
			res[index] = val

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