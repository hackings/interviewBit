class Solution:
	# @param A : string
	# @return a list of list of strings
	def partition(self, A):
		res = []
		self.helper(res, [], A, 0)
		return res
	def helper(self, res, cur, A, i):
		if i == len(A):
			res.append(list(cur))

		for j in xrange(i, len(A)):
			if self.isPalindrome(A[i:j+1]):
				cur.append(A[i:j+1])
				self.helper(res, cur, A, j+1)
				cur.pop()
	def isPalindrome(self, A):
		return list(A) == list(reversed(A))
"""
Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
"""