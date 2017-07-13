# [0, 1, 2, 3, 4, 5 ,6, 7]
# [i, j, k, ............l]
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
	def fourSum(self, A, B):
		A = sorted(A)
		res = set([])
		for i in xrange(len(A)-3):
			for j in xrange(i+1, len(A)-2):
				k = j+1
				l = len(A)-1
				while k < l:
					temp_sum = A[i] + A[j] + A[k] + A[l]
					if temp_sum == B:
						res.add((A[i], A[j], A[k], A[l]))
						k += 1
					elif temp_sum < B:
						k += 1
					else:
						l -= 1
		return sorted(res)
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

 Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example : 
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:

	(-2, -1, 1, 2)
	(-2,  0, 0, 2)
	(-1,  0, 0, 1)
Also make sure that the solution set is lexicographically sorted.
Solution[i] < Solution[j] iff Solution[i][0] < Solution[j][0] OR (Solution[i][0] == Solution[j][0] AND ... Solution[i][k] < Solution[j][k])


-----


When the array is sorted, try to fix the least and second least integer by looping over it.
Lets say the least integer in the solution is arr[i] and second least is arr[j].
Now we need to find a pair of integers k and l such that arr[k] + arr[l] is target-arr[i]-arr[j]. 
To do that, lets try the 2 pointer approach. If we fix the two pointers at the end ( that is, j+1 and end of array ), we look at the sum.
If the sum is smaller than the sum we want, we increase the first pointer to increase the sum.
If the sum is bigger than the sum we want, we decrease the end pointer to reduce the sum.

Note that there is one more solution possible if the question only asked to answer YES / NO to suggest whether there existed atleast one tuple with the target sum. 
Then we could have gone with an approach using more memory with hashing.

"""