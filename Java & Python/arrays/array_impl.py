def performOps(A):
    blen = 2 * len(A)
    B = [0]*blen
    for i in xrange(len(A)):
        B[i] = A[i]
        B[i + len(A)] = A[(len(A) - i) % len(A)]
    return B


# A : [5, 10, 2, 1]
# blen = [0,0,0,0,0,0,0,0]
# B = [5,10,2,1, A[(4-0)%4],A[(4-1)%4],A[(4-2)%4],A[(4-3)%4]]
# B = [5,10,2,1,A[0],A[3],A[2],A[1]]
# B = [5,10,2,1,5,1,2,10]