class Solution:
	# @param A : tuple of strings
	# @return an integer
	def isValidSudoku(self, A):
		rows = [[False for i in xrange(9)] for j in xrange(9)]
		cols = [[False for i in xrange(9)] for j in xrange(9)]
		grids = [[False for i in xrange(9)] for j in xrange(9)]

		for i in xrange(9):
			for j in xrange(9):
				if A[i][j] == '.':
					continue
				num = int(A[i][j])-1 	# 0-8 instead of 1-9 to match indexes
				grid = (i/3)*3 + (j/3)
				if rows[i][num] or cols[j][num] or grids[grid][num]:
					return 0
				else:
					rows[i][num], cols[j][num], grids[grid][num] = True, True, True
		return 1

"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character ‘.’.



The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""