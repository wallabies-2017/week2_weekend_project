
from models import Game
import view


class Controller:

	def __init__(self, app, view):
		self.app = app
		self.view = view
	
	def set_up(self):
		for i in range(2):
			you_ship_coord_direct = self.view.begin(False, None, None, i)
			if i==0:
				self.app.player_setup(you_ship_coord_direct[0])
			else:
				self.app.player2_setup(you_ship_coord_direct[0])
			while not self.app.place_ships(i, you_ship_coord_direct[1], 5, you_ship_coord_direct[2], you_ship_coord_direct[3]):
				you_ship_coord_direct = self.view.begin(True, you_ship_coord_direct[0], you_ship_coord_direct[1], i)
			# ship_sizes = [4, 3, 3, 2]
			# for size in ship_sizes:
			# 	your_board = self.app.print_boards(i)
			# 	nam_cord_direc = self.view.next_setup(size, your_board, False, i)
			# 	while not self.app.place_ships(i, nam_cord_direc[0], size, nam_cord_direc[1], nam_cord_direc[2]):
			# 		nam_cord_direc = self.view.next_setup(size, your_board, True, i)
			your_board = self.app.players[i].board._board
			self.view.pass_game(your_board, i)

	# def print_boards(player, enemy)
 #        return [self.players[player].get_board(), self.players[enemy].get_board()]

 #    def turn(self, enemy, coords):

	def turn(self):
		turn = 0
		other = 1
		while self.app.check_game_over():
			player, enemy = self.app.print_boards(turn, other)
			coords = self.view.turn(False, turn, player, enemy)
			while not self.app.turn(other, coords):
				coords = self.view.turn(True, turn, your_board, enemy_board)
			temp = turn
			turn = other
			other = temp


	def play(self):
		self.set_up()
		self.turn()


def main():
	controller = Controller(Game(), view)
	controller.play()

if __name__ == '__main__':
	main()