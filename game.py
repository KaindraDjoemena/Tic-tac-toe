"""
By: Kaindra Djoemena
GitHub: KaindraDjoemena [https://github.com/KaindraDjoemena]
Instagram: @yeahnicebro [https://www.instagram.com/yeahniceonebro/]

"""

# Importing the Board and the Players
from board import Board
from player import Player, User, Random_player, Minimax_player

# The game function
def game(board, x_player, o_player):
	current_player = x_player # Gives turns to the players

	board.printNumBoard()

	# Loops while the board has at least 1 empty space
	while board.thereIsEmptySpace():

		# Asks for input if the current player is a user
		current_player.getInput() if current_player.type == "u" else current_player.markSpace()

		print() # Prints the board
		board.printBoard()

		# Checks for wins
		if board.currentResult() == current_player.mark:
			print(f"\n{board.currentResult()} won")
			return "win" # Returns a random value to quit the function

		# Changes the player every turn
		if current_player == x_player:
			current_player = o_player
		elif current_player == o_player:
			current_player = x_player

	print("tie")


if __name__ == "__main__":
	game_board = Board() # The board object
	
	# user1 = User("X", game_board)
	# user1 = Random_player("X", game_board)
	# user1 = Minimax_player("X", game_board)

	# user2 = User("O", game_board)
	# user2 = Random_player("O", game_board)
	# user2 = Minimax_player("O", game_board)

	game(game_board, user1, user2)
