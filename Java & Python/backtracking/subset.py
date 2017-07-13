# 2 for loops, one for every int, one for every item in result
# [] [1] | [] + [2], [1] + [2]
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsets(self, s):
		s.sort()
		res = [[]]
		for e in s:
			res += [x+[e] for x in res]
		return sorted(res)
"""
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
"""