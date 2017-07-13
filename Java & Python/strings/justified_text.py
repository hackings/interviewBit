# concept there
class Solution:
	# @param A : list of strings
	# @param B : integer
	# @return a list of strings
	def fullJustify(self, A, B):
		res = []
		i, k, l = 0, 0, 0				# k - index of A
		while i < len(A):
			k, l = 0, 0
			while (i+k < len(A) and l + len(A[i+k]) ) <= B-k:
				l += len(A[i+k])
				k += 1
			temp = A[i]
			for j in xrange(k-1):
				if i+k >= len(A):
					temp += " "
				else:
					temp += str( (B-l)/(k-1) + (j < (B-l) % (k-1)) ).join(' ')
				temp += A[i+j+1]
			temp += str(B - len(A)).join(' ')
			res.append(temp)
			i += k
		return res

"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""