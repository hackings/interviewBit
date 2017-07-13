# Not working
class Solution:
	# @param A : integer
	# @return a list of list of integers
	def prettyPrint(self, A):
		rows, cols = 2*A-1, 2*A-1
		result = [rows][cols]

		top, left = 0, 0
		bottom, right = rows-1, cols-1

		direction, CONST_RIGHT = 0
		CONST_DOWN = 1
		CONST_LEFT = 2
		CONST_UP = 3
		num = A
		while top <= bottom and left <= right and num >= 0:
			if direction == CONST_RIGHT:
				for i in xrange(left, right+1):
					result[top][i] = num
				top += 1
				direction = CONST_DOWN

			elif direction == CONST_DOWN:
				for i in xrange(top, bottom+1):
					result[i][right] = num
				right -= 1
				direction = CONST_LEFT
			elif direction == CONST_LEFT:
				for i in xrange(right, left-1, -1):
					result[bottom][i] = num
				bottom -= 1
				direction = CONST_UP
			elif direction == CONST_UP:
				for i in xrange(bottom, top-1, -1):
					result[left][i] = num
				left += 1
				direction = CONST_RIGHT
				num -= 1
			else:
				continue
		
		for row in result:
			for column in row:
				print column
			print "\n"

"""
Input : 3
Output :
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
"""