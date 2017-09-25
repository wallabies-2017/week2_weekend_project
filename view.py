board_coord = [
['00','01','02','03','04','05','06','07','08','09'],
['10','11','12','13','14','15','16','17','18','19'],
['20','21','22','23','24','25','26','27','28','29'],
['30','31','32','33','34','35','36','37','38','39'],
['40','41','42','43','44','45','46','47','48','49'],
['50','51','52','53','54','55','56','57','58','59'],
['60','61','62','63','64','65','66','67','68','69'],
['70','71','72','73','74','75','76','77','78','79'],
['80','81','82','83','84','85','86','87','88','89'],
['90','91','92','93','94','95','96','97','98','99']]

def print_board(board):
	for i in range(10):
		print("| {}| {}| {}| {}| {}| {}| {}| {}| {}| {}|".format(*board_coord[i]))
		print("|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|_{}_|".format(*board[i]))

def begin(error, name=None, ship_name=None):
	if name is None:
		player = input("Please give me your name: ")
	else:
		player = name
	for row in board_coord:
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
	direct = input("please enter the orientation relative to this coordinate: east/west/north/south ")
	return [player, ship, coords, direct]

def next_setup(ship_len, your_board, error):
	print(your_board)
	# print_board(your_board)
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
