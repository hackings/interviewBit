class Solution:
	# @param A : integer
	# @return a boolean
	def isPower(self, A):
		if A <= 1:
			return True
		base = 2
		while base < A and base < sys.maxint / base:			# 2 - sys.maxint		base +1
			temp = base
			while temp <= A and temp < sys.maxint / base:		# 2*2 - sys.maxint		temp * base
				temp *= base
				if temp == A:
					return True
			base += 1
		return False

"""
Given a positive integer which fits in a 32 bit signed integer, 
find if it can be expressed as A^P where P > 1 and A > 0. 
A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 
"""