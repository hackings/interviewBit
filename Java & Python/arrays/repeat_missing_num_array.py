class Solution:
	# @param A : tuple of integers
	# @return a list of integers
	def repeatedNumber(self, A):
		_sum = squareSum = 0
		res = []
		for i in xrange(len(A)):
			temp = A[i]
			_sum += temp
			_sum -= i+1
			squareSum += temp*temp
			squareSum -= (i+1)*(i+1)

		# sum = A - B
       	# squareSum = A^2 - B^2 = (A - B)(A + B)
       	# squareSum / sum = A + B
		squareSum /= _sum

		A = int( (_sum+squareSum) / 2)
		B = squareSum - A
		res.append(A)
		res.append(B)
		return res
"""

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

------------

 Sum(Actual) = Sum(1...N) + A - B

    Sum(Actual) - Sum(1...N) = A - B. 

    Sum(Actual Squares) = Sum(1^2 ... N^2) + A^2 - B^2

    Sum(Actual Squares) - Sum(1^2 ... N^2) = (A - B)(A + B) 

    = (Sum(Actual) - Sum(1...N)) ( A + B). 
"""