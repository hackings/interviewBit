class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def paint(self, A, B, C):
		low = max(C)		# min amount of units 
		high = sum(C)
		while low < high:
			mid = low + (high-low)/2
			requiredPainters = self.reqPainters(C, mid)

			if requiredPainters <= A:
				high = mid
			else:
				low = mid+1
		return B*low%10000003
	def reqPainters(self, A, mid):
		total = 0
		numPainters = 1
		for i in xrange(len(A)):
			total += A[i]
			if total > mid:
				total = A[i]
				numPainters += 1
		return numPainters
"""

You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003

Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board

Output:
     return minimum time to paint all boards % 10000003
Example

Input : 
  K : 2
  T : 5
  L : [1, 10]
Output : 50
"""