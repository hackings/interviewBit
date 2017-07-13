# Error -     num += int(res[currentIndex])
# ValueError: invalid literal for int() with base 10: ''

# 2 for loops, multiply last numbers against each other
# currentIndex on A, index on B, add currentIndex val to res[currentIndex]
# reverse res, ''.join(res[i:])

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def multiply(self, A, B):
		res = []
		index_a = self.remove_whitespace(A)
		index_b = self.remove_whitespace(B)
		A[index_a:]
		B[index_b:]
		carry, index = 0, 0

		for i in xrange(len(A)-1, -1, -1):
			num = 0
			currentIndex = index
			for j in xrange(len(B)-1, -1, -1):
				num = int(A[i]) * int(B[j]) + carry
				carry = num / 10
				num %= 10
				char_number = chr(num)

				if currentIndex >= len(res):
					res.append(char_number)
				else:
					num += int(res[currentIndex])
					carry += num/10
					num %= 10
					char_number = chr(num)
					res[currentIndex] = char_number
				currentIndex += 1
			char_number = str(carry)
			carry = 0
			res.append(char_number)
			index += 1

		res.reverse()
		i = self.remove_whitespace(res)
		if i == len(res):
			return '0'

		return ''.join(res[i:])

	def remove_whitespace(self, A):
		i = 0
		while i < len(A) and A[i] == '0':
			i += 1
		return i
"""

Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.


"""