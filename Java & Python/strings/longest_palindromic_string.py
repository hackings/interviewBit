# racecar vs. raccar, depending on positions,
# for loop string, expand outwards from i,i or i,i+1
class Solution:
	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
		if A is None:
			return ""
		longest = A[0:1]	# a single char itself is palindrome
		for i in xrange(len(A)-1):
			p1 = self.expandAroundCenter(A, i, i)
			if len(p1) > len(longest):
				longest = p1

			p2 = self.expandAroundCenter(A, i, i+1)
			if len(p2) > len(longest):
				longest = p2
		return longest
	def expandAroundCenter(self, A, left, right):
		while (left >= 0 and right < len(A) and A[left] == A[right]):
			left -= 1
			right += 1
		return A[left+1:right]

"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
"""