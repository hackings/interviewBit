# for i, for j, haystack[i+j] != needle[j], isMatch = false

class Solution:
	# @param haystack : string
	# @param needle : string
	# @return an integer
	def strStr(self, haystack, needle):
		if len(haystack) == 0 or len(needle) == 0:
			return -1
		if len(needle) > len(haystack):
			return -1
		for i in xrange(len(haystack)):
			isMatched = True
			for j in xrange(len(needle)):
				if i+j > len(haystack)-1:
					return -1
				if haystack[i+j] != needle[j]:
					isMatched = False
					break
			if isMatched == True:
				return i
		return -1

"""
Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ). 
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""