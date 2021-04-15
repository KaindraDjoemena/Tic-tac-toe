"""
By: Kaindra Djoemena
GitHub: KaindraDjoemena [https://github.com/KaindraDjoemena]
Instagram: @yeahnicebro [https://www.instagram.com/yeahniceonebro/]


"""

import math
import random
from random import choices

# The player class
class Player:
	def __init__(self, mark, game_board):
		self.mark = mark # The mark of the player
		self.game_board = game_board


# These classes inherits form the player class
class User(Player):
	def __init__(self, mark, board):
		super().__init__(mark, board)
		self.type = "u"

	# Marks a space
	def markSpace(self, coordinate, mark):

		# Validates the inputs
		if self.markingIsValid(coordinate):
			coordinate = int(coordinate)

			# Assigning the input to the coordinate
			for i in range(3):
				for j in range(3):
					if coordinate == self.game_board.num_board[i][j]:
						self.game_board.board[i][j] = mark
						print(f"{self.mark} to {self.game_board.num_board[i][i]}")
			return True
		return False

	# Returns True if the input is valid
	def markingIsValid(self, coordinate):

		# Returns True if the coordinate/num is a digit from 0-8 and the value of that
		# number on the board is a " "
		if coordinate.isdigit():
			coordinate = int(coordinate)
			for i in range(3):
				for j in range(3):
					if coordinate == self.game_board.num_board[i][j]:
						if self.game_board.board[i][j] == " ":
							return True
		return False

	# Gets the input from the user
	def getInput(self):
		while True:
			user_input = input(f"{self.mark}'s turn: ")
			input_is_valid = self.markSpace(user_input, self.mark)
			if input_is_valid: # Breaks out of the loop if the input is valid
				break
			print("invalid input. Try again")


class Random_player(Player):
	def __init__(self, mark, board):
		super().__init__(mark, board)
		self.type = "r"

	# Marks a random space
	def markSpace(self):
		# Keeps on looping until the random space is a " " so the random user can assing a mark to it
		while True:
			points = [x for x in range(3)]
			random_i = random.choice(points)
			random_j = random.choice(points)
			if self.game_board.board[random_i][random_j] == " ":
				self.game_board.board[random_i][random_j] = self.mark
				print(f"{self.mark} to {self.game_board.num_board[random_i][random_j]}")
				break


class Minimax_player(Player):
	def __init__(self, mark, board):
		super().__init__(mark, board)
		self.type = "m"

		# Determining the other player's mark
		if self.mark == "X":
			self.other_player_mark = "O"
		elif self.mark == "O":
			self.other_player_mark = "X"

		# Lookup table to access the values
		self.score_lookup = {
			self.mark: 1,
			self.other_player_mark: -1,
			"tie": 0
		}
	
	# Marks the space differently depending on the state of the board
	def markSpace(self):

		# If the minimax player goes first, then pick a random space
		if self.game_board.numOfEmptySpaces() == 9:
			points = [x for x in range(3)]
			random_i = random.choice(points)
			random_j = random.choice(points)
			self.game_board.board[random_i][random_j] = self.mark

		# Otherwise, use the minimax function to pick the optimal space
		else:
			best_score = -math.inf # Best score is infinitely small
			for i in range(3):
				for j in range(3):
					# Do the operation if the space is empty
					if self.game_board.board[i][j] == " ":

						self.game_board.board[i][j] = self.mark # Assign self.mark on the possible spaces

						score = self.minimax(False) # Calculate the score

						self.game_board.board[i][j] = " " # Undo the assignment

						# best_score is the biggest value out of the 3 possible
						# outcomes => (1, 0, -1)
						# best_score can't be worse than it is because it'll only
						# be overwritten once the value is bigger than it's current value
						if score > best_score:
							best_score = score
							optimal_coordinate = (i, j)

			# Assigning self.mark to the optimal space
			self.game_board.board[optimal_coordinate[0]][optimal_coordinate[1]] = self.mark
			print(f"{self.mark} to {self.game_board.num_board[optimal_coordinate[0]][optimal_coordinate[1]]}")

	# The minimax function calculates the best score to determine the optimal move
	def minimax(self, maximizing):

		# Returns the score depending on the result of the current board
		current_result = self.game_board.currentResult()
		if current_result != None:
			return self.score_lookup[current_result]
		
		# Maximizing
		if maximizing:
			best_score = -math.inf # The initial best score is infinitely small
			for i in range(3):
				for j in range(3):
					if self.game_board.board[i][j] == " ":

						self.game_board.board[i][j] = self.mark # Assings the max mark to the space

						score = self.minimax(False) # Minimize
						self.game_board.board[i][j] = " " # Undo

						# best_score is the biggest value out of the 3 possible
						# outcomes => (1, 0, -1)
						best_score = max(score, best_score)
			return best_score # Return the best score(biggest)

		# Minimizing
		else:
			best_score = math.inf # The initial best score is infinitely big
			for i in range(3):
				for j in range(3):
					if self.game_board.board[i][j] == " ":

						self.game_board.board[i][j] = self.other_player_mark # Assings the opponents mark to the space

						score = self.minimax(True) # Maximize
						self.game_board.board[i][j] = " " # Undo
						
						# best_score is the smallest value out of the 3 possible
						# outcomes => (1, 0, -1)
						best_score = min(score, best_score)
			return best_score # Return the best score(smallest)
