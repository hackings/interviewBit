class Solution:
	# @param A : string
	# @return a list of strings
	def restoreIpAddresses(self, A):
		res, i, A = [], 1, A.strip()
		if len(A) > 12 and len(A) < 4:
			return []
		while i <= 3 and i < len(A):
			j = i+1
			while j <= i+3 and j < len(A):
				k = j+1
				while k <= j+3 and k < len(A):
					#print A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:]
					a = int(A[:i])
					b = int(A[i:j])
					c = int(A[j:k])
					d = int(A[k:])
					if ( (A[0] == '0' and (i > 1 or a != 0) )
						or 	(A[i] == '0' and (j > i+1 or b != 0))
						or 	(A[j] == '0' and (k > j+1 or c != 0))
						or  (A[k]) == '0' and (len(A) > k+1 or d != 0)):
						k += 1 		# do nothing
						continue
					elif ( 	a <= 255 and a >= 0
						and	b <= 255 and b >= 0
						and c <= 255 and c >= 0
						and d <= 255 and d >= 0
						):
						res.append(A[:i]+"."+A[i:j]+"."+A[j:k]+"."+A[k:])
					k += 1
				j += 1
			i += 1
		return res

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""