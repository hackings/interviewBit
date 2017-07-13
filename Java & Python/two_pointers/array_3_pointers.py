# min = min(A[i], B[j], C[k])
# max = max(A[i], B[j], C[k])
# if diff == 0, return diff
# if min == A[i], ++i, etc. etc.
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @param C : tuple of integers
	# @return an integer
	def minimize(self, A, B, C):
		diff = sys.maxint
		i, j, k = 0, 0, 0
		while i < len(A) and j < len(B) and k < len(C):
			minimum = min(A[i], min(B[j], C[k]))
			maximum = max(A[i], max(B[j], C[k]))
			diff = min(diff, maximum-minimum)
			if diff == 0:
				break

			if A[i] == minimum:
				i += 1
			elif B[j] == minimum:
				j += 1
			else:
				k += 1
		return diff

"""
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
Example :

Input : 
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5 
         With 10 from A, 15 from B and 10 from C. 
"""