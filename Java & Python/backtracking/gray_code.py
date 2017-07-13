# ( i shift right ) XOR i
class Solution:
	# @param A : integer
	# @return a list of integers
	def grayCode(self, A):
		res = []
		for i in xrange(2**A):		# 2 ^ A
			res.append( (i >> 1)^i )	# x shifted right by n bits, ^ = XOR
		return res
"""
i = 4
100 = 010 ^ 100 = 110 = 6

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.
Return any such sequence.
"""