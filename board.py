"""
By: Kaindra Djoemena
GitHub: KaindraDjoemena [https://github.com/KaindraDjoemena]
Instagram: @yeahnicebro [https://www.instagram.com/yeahniceonebro/]

"""

# The board class
class Board:
	def __init__(self):
		# Empty board
		self.board = [
			[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]
		]
		self.num_board = self.makeBoardWithNums() # Assigning the num board to self.num_board
		self.current_winner = None

	# Makes a board with numbers
	def makeBoardWithNums(self):
		board_with_nums = []
		for n in range(3):
			n *= 3
			row = [x for x in range(0+n, 3+n)]
			board_with_nums.append(row)
		return board_with_nums

	# Prints the board
	def printBoard(self):
		for i in range(3):
			print("[ " + self.board[i][0] + " ][ " + self.board[i][1] + " ][ " + self.board[i][2] + " ]")

	# Counts the amount of empty spaces
	def numOfEmptySpaces(self):
		empty_squares = 0
		for i in range(3):
			for j in range(3):
				if self.board[i][j] == " ":
					empty_squares += 1
		return empty_squares

	# Returns True if there's an empty space
	def thereIsEmptySpace(self):
		for i in range(3):
			for j in range(3):
				if " " == self.board[i][j]:
					return True
		return False

	# Checks if the three inputs are the same but not equal to " "
	def validThrees(self, x, y, z):
		if x == y == z != " ":
			return True
		return False

	# Returns the current result of the board
	def currentResult(self):
		self.current_winner = None

		# Counting the number of empty spaces
		empty_squares = self.numOfEmptySpaces()

		# Diagonals
		if self.validThrees(self.board[0][0], self.board[1][1], self.board[2][2]):
			self.current_winner = self.board[0][0]

		elif self.validThrees(self.board[0][2], self.board[1][1], self.board[2][0]):
			self.current_winner = self.board[0][2]

		# Rows
		for i in range(3):
			if self.validThrees(self.board[i][0], self.board[i][1], self.board[i][2]):
				self.current_winner = self.board[i][0]

		# Columns
		for i in range(3):
			if self.validThrees(self.board[0][i], self.board[1][i], self.board[2][i]):
				self.current_winner = self.board[0][i]
		
		if (self.current_winner == None) and (empty_squares == 0):
			return "tie"
		else:
			return self.current_winner
		return None
