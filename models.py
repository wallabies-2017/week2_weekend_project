BOARD_SIZE = 10
EMPTY_CELL="_"
SHIP="S"
HIT="X"
MISS="O"


class Board:
    def __init__(self):
        self._board = self.creat_board()
        self.ships = []
        self.shots = set()

    def creat_board(self):
        return [[EMPTY_CELL]*BOARD_SIZE for _ in range(BOARD_SIZE)]

    def shoot(self, coord):
        spot=self._board[coord[0]][coord[1]]
        print(coord)
        if self.valid_coord(coord) and coord not in self.shots:
            self.shots.add(coord)
            if spot == EMPTY_CELL:
                self._board[coord[0]][coord[1]]=MISS
                return True
            elif isinstance(spot, Ship):
                self._board[coord[0]][coord[1]]=HIT
                spot.hit()
                return True
        return False


    def gen_coords(self, size, coord, direction):
        coordinates = []
        if direction=="east":
            delta = (0,1)
        if direction=="west":
            delta = (0,-1)
        if direction=="north":
            delta = (-1,0)
        if direction=="south":
            delta = (1,0)
        for i in range(size):
            coordinate = (coord[0] + delta[0]*i, coord[1] + delta[1]*i)
            if self.valid_coord(coordinate):
                coordinates.append(coordinate)
            else:
                return None
        return coordinates


    def valid_coord(self, coord):
        valid_range = range(BOARD_SIZE)
        return all(point in valid_range for point in coord)


    def is_empty(self, coord):
        if self._board[coord[0]][coord[1]] != EMPTY_CELL:
            return False
        else:
            return True


    def add_ship(self, ship, coord, direction):
        coordinates = self.gen_coords(ship.size, coord, direction)
        if coordinates and all(self.is_empty(coordinate) for coordinate in coordinates):
            self.place_ship(ship, coordinates)
            self.ships.append(ship)
            return True
        else:
            return False

    def place_ship(self, ship, coordinates):
        for row, col in coordinates:
            self._board[row][col] = ship
        return True

    def is_game_over(self):
        return all(ship.is_sunk() for ship in self.ships)

    def get_board(self):
        return self._board

    def creat_represen(self):
        matrix = [[EMPTY_CELL]*BOARD_SIZE for _ in range(BOARD_SIZE)]
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if not isinstance(self._board[i][j], str):
                    matrix[i][j] = 'S'
                else:
                    matrix[i][j] = self._board[i][j]
        return matrix

class Ship:
    def __init__(self,size,name,hits=0):
        self.size=size
        self.hits=hits
        self.name=name

    def __str__(self):
        return "S"
        # "<Ship: size={}, name={}, hits={}>".format(
        #     repr(self.size), repr(self.name), repr(self.type), repr(self.hits)
        # )

    # def __repr__(self):
    #     return "Ship(size={}, name={}, type={}, hits={})".format(
    #         repr(self.size), repr(self.name), repr(self.type), repr(self.hits)
    #     )

    def is_sunk(self):
        if self.size == self.hits:
            return True
        return False

    def hit(self):
        if not self.is_sunk():
            self.hits+=1
            return True
        return False

class Player:
    def __init__(self,name):
        self.name=name
        self.board=Board()

    def add_ship(self, ship, coord, direction):
        return self.board.add_ship(ship, coord, direction)

    def shoot(self, coord):
        return self.board.shoot(coord)

    def get_board(self):
        return self.board.creat_represen()


class Game:
    def __init__(self):
        self.players=[]
        self.num_ships=5

    def setup(self, num_players):
        pass

    def player_setup(self, name):
        self.players.append(None)
        self.players[0] = Player(name)

    def player2_setup(self, name):
        self.players.append(None)
        self.players[1] = Player(name) 

    def place_ships(self, player, name, size, coord, direction):
        ship = Ship(size, name)
        if self.players[player].add_ship(ship, coord, direction):
            return self.players[player].get_board()
        else:
            return False

    def print_boards(self, player, enemy=None):
        if enemy is not None:
            return [self.players[player].get_board(), self.players[enemy].get_board()]
        else:
            return self.players[player].get_board()

    def turn(self, enemy, coords):
        if self.players[enemy].shoot(coords):
            return True
        else:
            return False


    def check_game_over(self):
        return True

# def main():
#     import pprint
#     base = "Ship"
#     ships = [Ship(i, base + str(i), base + str(i)) for i in range(2, 6)]
#     #print(ships)
#     board=Board()
#     coords=[{(0,0):"east"},{(9,9):"north"},{(5,5):"west"},{(3,7):"south"},{(7,3):"east"}]
#     for ship,coord in zip(ships,coords):
#         val, *_=coord.items()
#         board.add_ship(ship,*val)
#     # pprint.pprint(board.get_board())
#     # board.shoot((0,0))
#     # pprint.pprint(board.get_board())
#     return board.get_board()

# if __name__ == '__main__':
#     board=main()
