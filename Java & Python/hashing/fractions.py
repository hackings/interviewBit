# (remainder % denominator) * 10
# keep remainder in a dictionary
# d[.2525] = len(res), so you can insert () later
class Solution:
	# @param numerator : integer
	# @param denominator : integer
	# @return a string
	def fractionToDecimal(self, numerator, denominator):
		if numerator == 0:
			return "0"
		if denominator == 0:
			return ""
		res = ""
		# XOR 1 or other is negative
		if ((numerator < 0)^(denominator < 0)) == True:
			res = "-"
		numerator = abs(numerator)
		denominator = abs(denominator)

		res += str(numerator/denominator)
		remainder = (numerator % denominator)*10
		if remainder == 0:
			return res
		d = dict()
		res += "."
		while remainder != 0:
			if remainder in d:
				c = d[remainder]	# length of old result
				res = res[:c] + "(" + res[c:len(res)] + ")"		# .545454
				return res
			d[remainder] = len(res)
			res += str(remainder/denominator)
			remainder = (remainder % denominator) * 10
		return res
"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example :

Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)


1) multiply the remainder by 10, 
2) append remainder / denominator to your decimals
3) remainder = remainder % denominator.
At any moment, if your remainder becomes 0, you are done.
If you start with remainder = R at any point with denominator d, you will always get the same sequence of digits. 
So, if your remainder repeats at any point of time, you know that the digits between the last occurrence of R will keep repeating.
"""