# stack and delimit
class Solution:
	# @param A : string
	# @return a strings
	def simplifyPath(self, url):
		stack = []
		url = url.split('/')
		for c in url:
			if c == '..':
				if len(stack) > 0:
					stack.pop()
			elif c == '.':
				continue
			elif len(c) != 0:
				stack.append(c)
		return '/'+'/'.join(stack)



"""

Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
"""