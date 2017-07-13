class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
		stack = []
		tp, area_with_top, i, res = -1, -1, 0, 0
		while i < len(A):
			if len(stack) == 0 or A[i] >= A[stack[-1]]:
				stack.append(i)
				i += 1
			else:
				tp = stack.pop()
				if len(stack) == 0:
					area_with_top = A[tp] * i
				else:
					area_with_top = A[tp] * (i-stack[-1]-1)
				if res < area_with_top:
					res = area_with_top
		while len(stack) != 0:
			tp = stack.pop()
			if len(stack) == 0:
				area_with_top = A[tp] * i
			else:
				area_with_top = A[tp] * (i-stack[-1]-1)
			if res < area_with_top:
				res = area_with_top
		return res
"""
Given n non-negative integers representing the histogram’s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example Histogram

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

Example2

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""