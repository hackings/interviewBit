class Solution:
	# @param n : integer
	# @param k : integer
	# @return a strings
	def getPermutation(self, n, k):
		res, d = {0:1}, ""
		for i in xrange(1, n+1):
			d[i] = d[i-1]*i
		l = range(1, n+1)
		while k:
			i = k/d[len(l)-1]

			if i == len(l):
				res += str(l[-1])

"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"
Given n and k, return the kth permutation sequence.

For example, given n = 3, k = 4, ans = "231"

 Good questions to ask the interviewer :
What if n is greater than 10. How should multiple digit numbers be represented in string?
> In this case, just concatenate the number to the answer.
> so if n = 11, k = 1, ans = "1234567891011"
Whats the maximum value of n and k?
> In this case, k will be a positive integer thats less than INT_MAX.
> n is reasonable enough to make sure the answer does not bloat up a lot.
"""