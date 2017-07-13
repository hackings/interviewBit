class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def compareVersion(self, A, B):
		A = A.split('.')
		B = B.split('.')
		for i in xrange(len(A)):
			A[i] = int(A[i])
		for i in xrange(len(B)):
			B[i] = int(B[i])
		loopCount = min(len(A), len(B))

		for i in xrange(loopCount):
			if A[i] > B[i]:
				return 1
			if A[i] < B[i]:
				return -1
		if len(A) > len(B):
			if sum(A[len(B):]) > 0:
				return 1
		if len(A) < len(B):
			if sum(B[len(A):]) > 0:
				return -1
		return 0

"""
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""