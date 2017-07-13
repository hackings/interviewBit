class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def maxPoints(self, A, B):
		if len(A) <= 2:
			return len(A)
		res = 0
		for i in xrange(len(A)):
			d = {}
			duplicates = 1
			for j in xrange(len(A)):
				if A[i] == A[j] and B[i] == B[j] and i != j:
					duplicates += 1
				elif i != j:
					if A[i] == A[j]:		# vertical line, X's are same
						d['v'] = d.get('v', 0) + 1
					elif B[i] == B[j]:		# horizontal line, Y's are same
						d['h'] = d.get('h', 0) + 1	# dict.get(key, default=None)
					else:
						slope = 1.0*(B[i]-B[j])/(A[i]-A[j])	# Y2-Y1 / X2-X1
						d[slope] = d.get(slope, 0) + 1
			if len(d) > 0:
				res = max(res, max(d.values()) + duplicates)
			else: 				# if all points are duplicates, d is empty
				res = max(res, duplicates)
		return res




"""

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :

(1, 1)
(2, 2)
Sample Output :

2
You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])
"""