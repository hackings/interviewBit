class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A[-1] += 1
        temp = 0
        tempSum = 0
        for i in range(len(A)-1,-1,-1):
            tempSum = A[i]+temp     # carry the one over
            A[i] = tempSum%10
            temp = (A[i]+temp)/10
            
        if temp > 0:
            A = [temp] + A
        i = 0
        while i < len(A):   # get rid of 00000123
            if A[i] > 0:
                break
            i += 1
        return A[i:]


"""
Time Complexity - O(N)
[9,9]
[9,10]
tempSum = 10 + 0
temp = 10/10 = 1
A = [9, 0]
tempSum = 9 + 1
temp = (9+1)/10 = 1
A[1] = 10%10 = 0
[0, 0]

if temp > 0:
    [1,0,0]


[1,2,3]
[1,2,4]
tempSum = 4 + 0
temp = 4/10 = 0
A[2] = 4
tempSum = 2 + 0
temp = 2/10
A[2] = 2

# range(start, stop[, step])
"""