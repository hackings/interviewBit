# Concept, doesn't pass
# for loop - swap (start,i), then permute [i-end], swap(start,i)
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, a):
		Solution.result = []
		self.permute_helper(a, 0)
		return Solution.result
	def permute_helper(self, a, start):
		if start == len(a)-1:
			Solution.result.append(a)	# prints out correctly but result doesn't gett passed back in?
		for i in xrange(start, len(a)):
			a[start], a[i] = a[i], a[start]
			self.permute_helper(a, start+1)
			a[start], a[i] = a[i], a[start]

"""
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
"""
