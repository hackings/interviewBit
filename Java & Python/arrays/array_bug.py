class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    # rotate the array A by B positions.
    # A : [1 2 3 4 5 6]
	# B : 1
	# output : [2 3 4 5 6 1]
    def rotateArray(self, a, b):
        ret = []
        
        for i in xrange(len(a)):
            newIndex = (i+b) % len(a)
            ret.append(a[newIndex])
            
        return ret
