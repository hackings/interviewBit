# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# Given n = 3, return the following matrix:
# 1 2 3
# 8 9 4
# 7 6 5
# [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ] 
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
    	square_matrix = [[0 for i in xrange(A)] for j in xrange(A)]
    	count = 1
    	rows = A
    	cols = A

    	top = 0
    	right = cols-1
    	left = 0
    	bottom = rows-1

    	CONST_RIGHT = 0
    	CONST_DOWN = 1
    	CONST_LEFT = 2
    	CONST_UP = 3

    	direction = CONST_RIGHT

    	while top <= bottom and left <= right:
    		if direction is CONST_RIGHT:
    			for i in xrange(left,right):
    				square_matrix[top][i] = count
    				count += 1
    			top += 1
    		elif direction is CONST_DOWN:
    			for i in xrange(top, bottom):
    				square_matrix[i][right] = count
    				count += 1
    			right -= 1
    		elif direction is CONST_LEFT:
    			for i in reversed(xrange(left,right)):
    				square_matrix[bottom][i] = count
    				count += 1
    			bottom -= 1
    		elif direction is CONST_UP:
    			for i in reversed(xrange(top,bottom)):
    				square_matrix[i][left] = count
    				count += 1
    			left += 1
    	direction = (direction + 1) % 4
    	return square_matrix

    	