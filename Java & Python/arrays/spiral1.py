# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    # direction = 0 - Right, 1 - Down, 2 Left, 3 Up
    def spiralOrder(self, A):
    	result = []
    	rows = len(A)
    	cols = len(A[0])

    	top = 0
    	bottom = rows-1
    	left = 0
    	right = cols-1

    	CONST_RIGHT = 0
    	CONST_DOWN = 1
    	CONST_LEFT = 2
    	CONST_UP = 3

    	direction = CONST_RIGHT

    	while top <= bottom and left <= right:
    		if direction == CONST_RIGHT:
    			for i in xrange(left,right+1):
    				result.append(A[top][i])
    			top += 1

    		elif direction == CONST_DOWN:
    			for i in xrange(top,bottom+1):
    				result.append(A[i][right])
    			right -= 1

    		elif direction == CONST_LEFT:
    			for i in xrange(right,left-1,-1):
    				result.append(A[bottom][i])
    			bottom -= 1

    		elif direction == CONST_UP:
    			for i in xrange(bottom,top-1,-1):
    				result.append(A[i][left])
    			left += 1

    		direction = (direction+1) % 4

        return result
