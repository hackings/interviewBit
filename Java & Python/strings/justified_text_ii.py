class Solution:
	# @param A : list of strings
	# @param B : integer
	# @return a list of strings
	def fullJustify(self, A, B):
		i, res = 0, []
		if len(A) == 0:
			return res
		while i < len(A):
			line, line_words, length = "", [], 0
			k = i
			while k < len(A):
				if length + len(line_words)+len(A[k]) <= B:
					line_words.append(A[k])
					length += len(A[k])
				else:
					break
				k += 1
			# print length, line_words, k
			i = k
			if k < len(A):
				if len(line_words) > 1:
					space = (B-length)/ (len(line_words)-1)
					remain = (B-length) % (len(line_words)-1)
					line += line_words[0]		# always append the first word
					line += " "*space
					if remain > 0:
						line += " "
					remain -= 1
					for j in xrange(1, len(line_words)-1):		# start from word 1 - line_words
						line += line_words[j]
						line += " "*space
						if remain > 0:
							line += " "
						remain -= 1
					if len(line_words) > 1:
						line += line_words[-1]
				else:
					line += line_words[0]
					line += " "*(B-len(line))
			else:								# k == len(A)
				line += line_words[0]			
				for j in xrange(1, len(line_words)):
					line += " " + line_words[j]
				line += " "*(B-len(line))
			res.append(line)
		return res

