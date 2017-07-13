# at end of row, row +=1 col = 0, else col += 1
# for loop, if you can put c, put c
# then call recursive function again until returns true
# if it doens't return true, put '.'
# canput function see if entire row or col has char
# see if if it's in rowGroup+3 and colGroup+3

class Solution:
	# @param A : list of list of chars
	# @return nothing
	def solveSudoku(self, board):
		self.solveSudokuRec(board, 0, 0)
	def solveSudokuRec(self, board, row, col):
		if row == 9:
			return True
		if col == 8:
			nextRow = row+1
			nextCol = 0
		else:
			nextRow = row
			nextCol = col+1
		if board[row][col] != '.':
			return self.solveSudokuRec(board, nextRow, nextCol)
		for c in xrange(1, 10):
			if self.canPut(board, str(c), row, col):
				board[row][col] = str(c)
				if self.solveSudokuRec(board, nextRow, nextCol):
					return True
				board[row][col] = '.'
		return False
	def canPut(self, board, char, row, col):
		for i in xrange(0, 9):
			if board[row][i] == char or board[i][col] == char:
				return False
	
			rowGroup = (row//3) * 3		# floor division 8 is in group 6-9
			colGroup = (col//3) * 3		# group 0, 3, 6
			for i in xrange(rowGroup, rowGroup + 3):
				for j in xrange(colGroup, colGroup+3):
					if board[i][j] == char:
						return False
		return True
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.' 
You may assume that there will be only one unique solution.



A sudoku puzzle,



and its solution numbers marked in red.

Example :

For the above given diagrams, the corresponding input to your program will be

[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]
and we would expect your program to modify the above array of array of characters to

[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
"""