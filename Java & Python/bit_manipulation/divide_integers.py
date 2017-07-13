# Need to review
class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def divide(self, A, B):
		res = 0
		p = abs(A)
		q = abs(B)
		count = 0
		while p >= q:
			count = 0
			while p >= (q << count):
				count += 1
			res += 1 << (count-1)
			p -= q << (count-1)
		if A == -2147483648 and B == -1:
			return 2147483647		# no idea why
		if A*B < 0:
			return -res
		return res