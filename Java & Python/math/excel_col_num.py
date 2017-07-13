class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
		res = 0
		for i in xrange(len(A)):
			res = res * 26 + (ord(A[i])-ord('A')+1)
		return res
"""
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

	A -> 1
	
	B -> 2
	
	C -> 3
	
	...
	
	Z -> 26
	
	AA -> 27
	
	AB -> 28 
"""	