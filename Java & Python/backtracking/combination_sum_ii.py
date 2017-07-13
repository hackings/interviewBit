# DFS recursion function
# inside a for loop from i - end, 0-end, 1-end, 2-end
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
	def combinationSum(self, A, target):
		A.sort()
		Solution.res = []
		self.DFS(A, target, 0, [])
		return Solution.res
	def DFS(self, A, target, start, valuelist):
		length = len(A)
		if target == 0 and valuelist not in Solution.res:
			return Solution.res.append(valuelist)
		for i in xrange(start, length):
			if target < 0:
				return
			self.DFS(A, target - A[i], i+1, valuelist + [A[i]])

"""

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""