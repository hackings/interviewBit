# concept
# instead swapping for permutation
# append to current from [0..i]
# permute
# pop back current from [0..i]
class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def subsetsWithDup(self, s):
		Solution.res = [[]]
		current = []
		s.sort()
		self.generateSubsets(s, 0, current)
		Solution.res.sort()
		return Solution.res

	def generateSubsets(self, s, index, current):
		if index >= len(s):
			Solution.res.append(current)
		currentIndex = index+1
		# find num repeats of s[index]
		while currentIndex < len(s) and s[currentIndex] == s[index]:
			currentIndex += 1

		# there are currentIndex - index # of repeating entries
		# loop over # entries to include in our subset
		for i in xrange(currentIndex-index + 1):
			for j in xrange(i):
				current.append(s[index])
			self.generateSubsets(s, currentIndex, current)
			for j in xrange(i):
				current.pop()