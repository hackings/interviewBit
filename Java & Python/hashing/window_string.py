class Solution:
	# @param S : string
	# @param T : string
	# @return a string
	def minWindow(self, S, T):
		counts = {c:0 for c in T}
		target_counts = {}
		for c in T:
			if c in target_counts:
				target_counts[c] += 1
			else:
				target_counts[c] = 1
				
		cover = 0
		shortest = None
		start, end = 0, 0
		while end < len(S) or cover == len(counts):
			if cover < len(counts):
				end += 1
				if S[end-1] in counts:
					if counts[S[end-1]] == target_counts[S[end-1]] - 1:
						cover += 1
					counts[S[end-1]] += 1
			else:
				if S[start] in counts:
					counts[S[start]] -= 1
					if counts[S[start]] == target_counts[S[start]] - 1:
						cover -= 1
				start += 1
			if cover == len(counts):
				if shortest is None or end-start < shortest[0]:
					shortest = end-start, start, end
		if shortest is None:
			return ''
		return S[shortest[1]:shortest[2]]
"""

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be atleast N.

Example :

S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).

------

Think 2 pointers and hashing.

Essentially you have a start and end pointer starting from the beginning of 
the string. You keep moving the end pointer and including more characters 
till you have all the characters of T included. At this point, you start 
moving start pointer and popping out characters till the point that you
still have all the characters of T included. Update your answer and keep 
repeating the process.

"""