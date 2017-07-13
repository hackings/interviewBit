# set
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsetsWithDup(self, s):
		mySet = set([])
		s.sort()
		res = [[]]
		for e in s:
			for x in res:
				if x+[e] not in mySet:
					mySet.add(x+[e])
					res += x+[e]
		return sorted(res)
"""

Given a collection of integers that might contain duplicates, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:

[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
"""