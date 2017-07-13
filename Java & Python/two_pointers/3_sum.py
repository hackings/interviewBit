# sort
# [0,1, .. len(A)-1]
# [i, j, .. k]
# sum = A[i]+A[j]+A[k]
# sum < target, j++ else k--
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, target):
		if len(A) == 0:
			return target	
		A.sort()
		minDiff = sys.maxint
		res = 0
		for i in xrange(len(A)):
			j = i+1
			k = len(A)-1
			while j < k:
				_sum = A[i]+A[j]+A[k]
				diff = abs(_sum - target)
				if diff == 0:
					return _sum
				if diff < minDiff:
					minDiff = diff
					res = _sum
				if _sum < target:
					j += 1
				else:
					k -= 1
		return res
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example: 
given array S = {-1 2 1 -4}, 
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
"""