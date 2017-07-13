class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        A = A.strip()
        A = A.split()
        A = A[::-1]
        return ' '.join(A)


"""
Given an input string, reverse the string word by word.

Example:

Given s = "the sky is blue",

return "blue is sky the".
"""