class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
    	A = A.strip()
    	A = A.split()
    	if len(A) == 0:
    		return 0
    	last_word = A[len(A)-1]
    	if len(last_word) == 0 or last_word == None:
    		return 0
    	else:
    		return len(last_word) 

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Given s = "Hello World",

return 5 as length("World") = 5.

Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once."""