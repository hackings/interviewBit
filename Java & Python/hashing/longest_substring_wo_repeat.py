class Solution:
	def lengthOfLongestSubstring(self, A):
		start = maxLength = 0
		d = dict()

		for i in xrange(len(A)):
			if A[i] in d and start <= d[A[i]]:		# start index < current index
				start = d[A[i]] + 1
			else:
				maxLength = max(maxLength, i-start+1)
			d[A[i]] = i
		return maxLength

"""
Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
"""