# Need to review
class Solution:
	# @param A : integer
	# @return a list of list of strings
	def solveNQueens(self, A):
		stack = [[(0, i)] for i in xrange(A)]
		res = []
		while stack:
			board = stack.pop()
			row = len(board)
			if row == A:
				res.append([''.join('Q' if i == c else '.' for i in xrange(A)) 
					for r, c in board])
			for col in xrange(A):
				if all(col != c and abs(row-r) != abs(col-c) for r, c in board):
					stack.append(board+[(row, col)])			# Return True if all elements of the iterable are true
		return res

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""