class Solution:
	# @param A : string
	# @return an integer
	def power(self, A):
		A = A.strip()
		n = len(A)
		A = list(A)
		if n == 0:
			return 0
		if n == 1 and A[0] == '1':
			return 0

		while not isOne(A):
			if not isEven(A):	# if odd, def not power of 2
				return 0
			A = divByTwo(A)
		return 1

def divByTwo(A):
	i = 0
	while i < len(A):
		val = int(A[i])
		if val >= 2:
			A[i] = str(val/2)
			i += 1
			if val % 2 != 0:
				A[i] = '1' + A[i]
		elif val == 1:
			A[i] = '0'
			i += 1
			A[i] = '1' + A[i]
		else:
			i += 1
	# get rid of 0's in front
	i = 0
	while i < len(A) and A[i] == '0':
		i += 1
	return A[i:]
def isOne(A):
	if len(A) == 1 and A[0] == '1':
		return True
	return False

def isEven(A):
	t = int(A[-1])
	return t % 2 == 0

"""
Find if Given number is power of 2 or not. 
More specifically, find if given number can be expressed as 2^k where k >= 1.

Input:

number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
Output:

return 1 if the number if a power of 2 
else return 0

Example:

Input : 128
Output : 1

----

Loop until n not equal to 1 and also n is even :
        n divided by 2
IF n is equal to 1
        return 1
ELSE 
    return 0
"""