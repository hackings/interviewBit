# stack, add every single item
# check if stack[0] >= A[i], pop from stack
class Solution:
	# @param arr : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
		res = [None] * len(A)
		stack = []

		for i in xrange(len(A)):
			while len(stack) != 0 and stack[0] >= A[i]:
				stack.pop(0)
			if len(stack) == 0:
				res[i] = -1
			else:
				res[i] = stack[0]
			stack.insert(0, A[i])
		return res

"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is maximum possible AND 
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.

Example:

Input : A : [4, 5, 2, 10]
Return : [-1, 4, -1, 2]

Example 2:

Input : A : [3, 2, 1]
Return : [-1, -1, -1]
"""