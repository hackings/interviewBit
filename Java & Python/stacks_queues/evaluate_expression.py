class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
		res, first, second = 0, 0, 0
		stack = []
		for a in A:
			if a == '+' or a == '-' or a == '/' or a == '*':
				if len(stack) < 2:
					return 0
				second = stack.pop()
				first = stack.pop()
				if a == '+':
					res = first + second
					stack.append(res)
				elif a == '-':
					res = first-second
					stack.append(res)
				elif a == '*':
					res = first * second
					stack.append(res)
				elif a == '/':
					res = first/second
					stack.append(res)
			else:
				stack.append(int(a))
		if len(stack) == 1:
			return stack[0]
		else:
			return 0
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 """