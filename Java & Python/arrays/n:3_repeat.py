
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def repeatedNumber(self, A):
		k = 3
		count = [0]*(k-1)
		cand = [-1]*(k-1)
		for i in xrange(len(A)):
			j = 0			
			while j < k-1:			# A[i] is checked if in cands
				if cand[j] == A[i]:
					count[j] += 1
					break
				j += 1
			if j == k-1:			# A[i] is not in cands
				l = 0				
				while l < k-1:
					if count[l] == 0:
						cand[l] = A[i]
						count[l] = 1
						break
					l += 1
				if l == k-1:		# No candidate is empty, ignore and reduce counts by 1
					for l in xrange(k-1):
						count[l] -= 1

		# check for actual counts of candidates
		for i in xrange(k-1):
			temp = cand[i]
			tempCount = 0
			for j in xrange(len(A)):
				if A[j] == temp:
					tempCount += 1
			if tempCount > len(A)/k:
				return temp
		return -1
"""
You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times. 

-----

It is important to note that if at a given time, you have 3 distinct element from the array, if you remove them from the array, your answer does not change.

Assume that we maintain 2 elements with their counts as we traverse along the array.

When we encounter a new element, there are 3 cases possible :

We don’t have 2 elements yet. So add this to the list with count as 1.

This element is different from the existing 2 elements. As we said before, we have 3 distinct numbers now. Removing them does not change the answer. So decrement 1 from count of 2 existing elements. If their count falls to 0, obviously its not a part of 2 elements anymore.

The new element is same as one of the 2 elements. Increment the count of that element.

Consequently, the answer will be one of the 2 elements left behind. If they are not the answer, then there is no element with count > N / 3.

"""