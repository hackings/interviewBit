# Kandane's Algorithm
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        current_sum = max_sum = A[0]

    	for num in A[1:]:
            current_sum = max(num, current_sum+num)
            max_sum = max(current_sum, max_sum)
            
        return max_sum