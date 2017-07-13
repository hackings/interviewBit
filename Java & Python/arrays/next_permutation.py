class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
    	firstChar = -1
    	n = len(A)
    	for i in xrange(n-2, -1, -1):
    		if A[i] < A[i+1]:
    			firstChar = i
    			break
    	if firstChar == -1:
    		return sorted(A)
    	
    	secondChar = left = firstChar + 1
    	right = n - 1

    	for i in xrange(left+1, right+1):
    		if A[firstChar] < A[i] and A[i] < A[secondChar]:
    			secondChar = i

    	A[firstChar], A[secondChar] = A[secondChar], A[firstChar]	# swap

    	A = A[:firstChar + 1] + sorted(A[firstChar+1:])
    	
    	return A

"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.

If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.

The replacement must be in-place, do not allocate extra memory.

Examples:

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

20, 50, 113 → 20, 113, 50
-------------------------------
0 1 2 3 4
---------
1 2 3 4 5

firstChar = 3
secondChar = 4
left = 4
right = 4

1 2 3 5 4
return A[0:4] - A[4:5]
"""