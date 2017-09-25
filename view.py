import board

player_setup = [board.template1, board.template2]
enemy_board = [board.template3, board.template4]

def print_board(board, who):
	for i in range(10):
		for j in range(10):
			if not isinstance(board[i][j], str):
				board[i][j] = 'S'
				player_setup[who][i][j] = '  '
		print("| {}| {}| {}| {}| {}| {}| {}| {}| {}| {}|".format(*player_setup[who][i]))
		print("|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|".format(*board[i]))

def begin(error, name=None, ship_name=None, who=None):
	if name is None:
		player = input("Please give me your name: ")
	else:
		player = name
	for row in player_setup[who]:
		print("| {}| {}| {}| {}| {}| {}| {}| {}| {}| {}|".format(*row))
		print("|___|___|___|___|___|___|___|___|___|___|")
	if error:
		print("Sorry, your last entry was incorrect, let's try again")
	print('The first ship is 5 spaces long,')
	if ship_name is None:
		ship = input("What would you like to call this ship? ")
	else:
		ship = ship_name
	print('first I will ask for intital coordinate then I will ask for the direction')
	incorrect = True
	while incorrect:
		coord = input("please enter the 2 digit coordinate, for top row don't forget the zero ")
		if len(coord)==2:	
			coords = list(coord)
			if all(num.isdigit() for num in coords):
				coords = [int(coords[0]), int(coords[1])]
				incorrect = False
	incorrect = True
	directions = ['north', 'south', 'east', 'west']
	while incorrect:
		direct = input("please enter the orientation relative to this coordinate: east/west/north/south ")
		if direct in directions:
			incorrect = False
	return [player, ship, coords, direct]

def next_setup(ship_len, your_board, error, who):
	print_board(your_board, who)
	if error:
		print("Sorry, your last entry was incorrect, let's try again")
	print('the next ship is {} spaces long,'.format(ship_len)) 
	ship_name = input("What would you like to call this ship? ")
	incorrect = True
	while incorrect:
		coord = input("please enter the 2 digit coordinate, for top row don't forget the zero ")
		if len(coord)==2:	
			coords = list(coord)
			if all(num.isdigit() for num in coords):
				coords = [int(coords[0]), int(coords[1])]
				incorrect = False
	direct = input("please enter the orientation relative to this coordinate: east/west/north/south ")
	return [ship_name, coords, direct]

def turn(first, error, your_board, enemy_board):
	if error:
		coord = input("INVALID SELECTION, please enter the 2 digit coordinate, for top row don't forget the zero ")
	else:
		print("your enemy attacks, the result of their attack is displayed here:")
		print_board(your_board)
		if first:
			print("you can retaliate, we don't have an areal view of their fleet")
			print("but with a few blind shots we can determine their layout")
		else:
			print(' ')
	print_board(enemy_board)
	coord = input("please enter the 2 digit coordinate, for top row don't forget the zero ")
	return coord

def pass_game(your_board, player):
	print_board(your_board, player)
	print("setup complete")
	if player==0:
		print('please pass the computer to the other player')
