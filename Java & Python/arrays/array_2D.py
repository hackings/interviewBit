def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in xrange(len(A)):
        B.append([0] * n)
        for j in xrange(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B
# Test case 
# A : [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
# Solution 4 3 2 1 8 7 6 5 12 11 10 9
# B[0][4-1-0] = B[0][3] = A[0][0]
# B[0][4-1-1] = B[0][2] = A[0][1]