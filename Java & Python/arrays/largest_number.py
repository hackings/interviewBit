# Concept correct
class Solution:
	# @param A : tuple of integers
	# @return a strings
	def largestNumber(self, A):
		res = ""
		s = []
		for i in xrange(len(A)):
			s.append(str(A[i]))
		# sorting
		sorted(s, cmp=self.compareNum)
		# appending sorted 
		for i in xrange(len(s)):
			res += s[i]
		pos = 0
		# extra 0's in front
		while res[pos] == '0' and pos + 1 < len(res):
			pos += 1
		return res[pos:]
	def compareNum(self, A, B):
		return A+B > B+A


"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""