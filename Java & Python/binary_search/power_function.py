class Solution:
	# @param x : integer
	# @param n : integer
	# @param d : integer
	# @return an integer
	def pow(self, base, n, d):
		# ( base^n ) % d
		if n == 0:
			return 1 % d 					# 2^0 = 1, 1 % d 
		res = 1
		while n > 0:
			if n%2 == 1:					# 3 % 2 = 1
				res = (res*base) % d		# (1 * 2)%3 = 2
				n -= 1 
			else:
				base = (base*base) % d		# base = (2*2)%2 = 0
				n /= 2
		if res < 0:
			res = (res+d) % d
		return res 

"""

Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
-- Examples --
4 ^ 4 % 2
base = 4*4 % 2 = 0
n = 1
res = 1*0 % 2 = 0

4 ^ 4 % 3
res = 1*4 % 3 = 1
n = 2

base = 4*4 % 3 = 1
n = 1
res = 1*1 % 3  = 1

-4 ^ 2 % 3 = 
res = -1
base = -1
res = -1*1 

wtf?
if res < 0
(-4 + 3) % 3 
(-1 + 3) % 3
(2 % 3) = 2
"""