# even after A[mid] = target, make high = mid-1 to see if there are lower occurences
# make low = firstOcc to find secondOcc
# even after A[mid] = target, make low = mid+1 to see if there are higher occurences
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        n = len(A)
        low = 0
        high = n-1
        firstOcc = -1
        while low <= high:
            mid = (low+high)/2
            if A[mid] == B:
                firstOcc = mid
                high =  mid-1       # still tries to find if there are lower first occurences
            elif A[mid] < B:
                low = mid+1
            else:
                high = mid-1
        if firstOcc == -1:
            return [-1,-1]
        low = firstOcc
        high = n-1
        secondOcc = -1
        while low <= high:
            mid = (low+high)/2
            if A[mid] == B:
                secondOcc = mid
                low = mid+1
            elif A[mid] < B:
                low = mid+1
            else:
                high = mid-1
        return [firstOcc, secondOcc]


"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]

and target value 8,

return [3, 4].
"""