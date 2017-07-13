class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
    	# 1000, 2000, 3000
    	M = ["", "M", "MM", "MMM"]
    	# 100, 200, ... 900
    	C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    	# 10, 20, ... 90
    	X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    	# 1, 2, 3, ... 9
    	I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    	res = M[A/1000] + C[(A%1000)/100] + X[(A%100)/10] + I[A%10]
    	return res

"""

Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

Input is guaranteed to be within the range from 1 to 3999.

Example :

Input : 5
Return : "V"

Input : 14
Return : "XIV"

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1,000
"""