# Need to review
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def repeatedNumber(self, A):
		if len(A) <= 1:
			return -1
		value_range = len(A)-1				# valuerange
		_range = int(value_range**0.5) 		# sqrt(n)	range
		if _range*_range < value_range:
			_range += 1
		hash_len = _range+1
		d = [0]*hash_len
		for i in xrange(len(A)):
			d[ (A[i]-1)/_range ]	+= 1

		repeatingRange = -1
		num_ranges = ( (value_range-1)/_range )+1

		i = 0
		while i < num_ranges and repeatingRange = -1:
			if i < num_ranges-1 or value_range % _range == 0:
				if d[i] > _range:
					repeatingRange = i
				else:
					if d[i] > value_range % _range:
						repeatingRange = i
		if repeatingRange == -1:
			return -1
		d = [0]*hash_len
		for i in xrange(len(A)):
			if (A[i]-1)/_range == repeatingRange:
				d[ (A[i]-1)%_range ] += 1
		for i in xrange(_range):
			if d[i] > 1:
				return repeatingRange * _range + i+1
		return -1 



"""
Given a read only array of n + 1 integers between 1 and n, 
find one number that repeats in linear time using less then O(n) space 
and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.
"""