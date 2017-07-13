class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
		if len(A) < 1:
			return ""
		prefix = A[0]
		prefix_length = len(prefix)
		for i in xrange(1, len(A)):
			j = 0
			while j < min(prefix_length, len(A[i])):
				if prefix[j] != A[i][j]:
					break
				j += 1
			if j < prefix_length:
				prefix  = prefix[:j]
				prefix_length = j
		return prefix


"""

Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
The answer would be “a”.
"""