# Find out the maximum sub-array of non negative numbers from an array.
# The sub-array should be continuous. That is, a sub-array created by choosing the 
# second and fourth element and skipping the third element is invalid.
# NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
# NOTE 2: If there is still a tie, then return the segment with minimum starting index
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
    	max_subarray = []
    	max_sum = 0
    	current_subarray = []
    	current_sum = 0
    	for num in A:
    		if num >= 0:
    			current_subarray.append(num)
    			current_sum += num
    			if current_sum > max_sum:
    				max_sum = current_sum
    				max_subarray = list(current_subarray)
    		else:
    			if len(current_subarray) > 0:

	    			if current_sum > max_sum:
	    				max_subarray = list(current_subarray)

	    			elif current_sum == max_sum:
	    				if len(current_subarray) == len(max_subarray):
	    					if min(current_subarray[0], max_subarray[0]) == current_subarray[0]:
	    						max_subarray = list(current_subarray)	

	    				elif max(len(current_subarray), len(max_subarray)) == len(current_subarray):
	    					max_subarray = list(current_subarray)

    			current_subarray = []
    			current_sum = 0
    	return max_subarray