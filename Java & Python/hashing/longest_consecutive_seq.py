class Solution:
	# @param num, a list of integer
	# @return an integer
	def longestConsecutive(self, A):
		dict = {x: False for x in A} # False = not visited
		maxLen = -1
		for i in dict:
			if dict[i] == False:
				curr = i+1
				len_right = 0
				while curr in dict:
					len_right += 1
					dict[curr] = True
					curr += 1
				curr = i-1
				len_left = 0
				while curr in dict:
					len_left += 1
					dict[curr] = True
					curr -= 1

				maxLen = max(maxLen, len_left + 1 + len_right)
		return maxLen
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example: 
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""