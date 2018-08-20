"""Python script to generate all possible moves of a knight in a chess board
from a given position."""
# pylint:disable=invalid-name

import argparse
import sys

from collections import OrderedDict


class Chessercise(object):
    """Class to find all possible knight moves from given position."""
    def __init__(self):
        """Constructor method."""
        self.size = [8, 8]
        self.width = self.size[0]
        self.height = self.size[1]

        self.board = []
        self.algebraic_notation = OrderedDict()
        self.set_keys()
        self.reverse_mapping = {
            v: k for k, v in self.algebraic_notation.items()}

        self.generate_chess_board()

    def set_keys(self):
        """ Set keys in algebraic notation dict."""
        self.algebraic_notation['a'] = 0
        self.algebraic_notation['b'] = 1
        self.algebraic_notation['c'] = 2
        self.algebraic_notation['d'] = 3
        self.algebraic_notation['e'] = 4
        self.algebraic_notation['f'] = 5
        self.algebraic_notation['g'] = 6
        self.algebraic_notation['h'] = 7

    def generate_chess_board(self):
        """
        Generates the board from give width and height
        """
        keys = list(self.algebraic_notation.keys())
        for i, _ in enumerate(keys):
            row = []
            for j in range(1, len(keys)+1):
                row.append(keys[i]+str(j))
            self.board.append(row)

    def find_coordinates(self, position):
        """Find actual coordinates from given algebraic position."""
        name, index = list(position)
        if (name not in self.algebraic_notation.keys()) \
                or (int(index) < 0) or (int(index) > 8):
            return None
        return self.algebraic_notation.get(name, None), int(index)-1

    def get_algebraic_coordinate(self, x, y):
        """Get algebraic notation of given chess board coordinate

        Arguments:
          x (int): X axis coordinate
          y (int): Y axis coordinate
        Returns(str): Algebraic notation.
        """
        if x < 0 or x > 8 or y < 0 or y > 8:
            return None
        name = self.reverse_mapping.get(x, None)
        index = y+1
        return str(name)+str(index)

    def find_queen_possible_moves(self, position):
        """
        Generates a list of legal moves for a queen to move in one step

        Arguments:
          position (str): algebraic position of the piece (e,g. - 'a2')
        Returns(str): All possible moves in algebraic notation
        (comma separated).
        """
        x, y = self.find_coordinates(position)

        poss_pos = []

        for i, j in zip(range(x+1, self.height), range(y+1, self.height)):
            poss_pos.append(self.get_algebraic_coordinate(i, j))

        for i, j in zip(range(x+1, self.height), range(y-1, -1, -1)):
            poss_pos.append(self.get_algebraic_coordinate(i, j))

        for i, j in zip(range(x-1, -1, -1), range(y+1, self.height)):
            poss_pos.append(self.get_algebraic_coordinate(i, j))

        for i, j in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
            poss_pos.append(self.get_algebraic_coordinate(i, j))

        queen_moves = ", ".join(poss_pos)
        rook_moves = self.find_rook_possible_moves(position)

        queen_all_moves = queen_moves+', '+rook_moves

        return queen_all_moves

    def find_rook_possible_moves(self, position):
        """
        Generates a list of legal moves for a rook to take in one step
        Arguments:
          position (str): algebraic position of the piece (e,g. - 'a2')
        Returns(str): All possible moves in algebraic
        notation(comma separated).
        """
        x, y = self.find_coordinates(position)
        poss_pos = []

        for i in range(0, x):
            poss_pos.append(self.get_algebraic_coordinate(i, y))

        for i in range(x+1, self.height):
            poss_pos.append(self.get_algebraic_coordinate(i, y))

        for i in range(0, y):
            poss_pos.append(self.get_algebraic_coordinate(x, i))

        for i in range(y+1, self.height):
            poss_pos.append(self.get_algebraic_coordinate(x, i))

        return ", ".join(poss_pos)

    def find_knight_possible_moves(self, position):
        """
        Generates a list of legal moves for a knight to take in next step

        Arguments:
          position (str): algebraic position of the piece (e,g. - 'a2')
        Returns(str): All possible moves in algebraic
        notation(comma separated).
        """
        knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1),
                        (-2, 1), (-2, -1)]
        x, y = self.find_coordinates(position)
        possible_pos = []

        for move in knight_moves:
            new_x = int(x + move[0])
            new_y = int(y + move[1])

            if new_x >= self.height:
                continue
            elif new_x < 0:
                continue
            elif new_y >= self.width:
                continue
            elif new_y < 0:
                continue
            else:
                possible_pos.append(self.get_algebraic_coordinate(new_x,
                                                                  new_y))

        return ", ".join(possible_pos)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--piece', type=str,
                        help='type of piece which is to be moved')

    parser.add_argument('--position', type=str,
                        help='Current position of the piece')
    args = parser.parse_args()

    type_of_piece = args.piece
    cur_pos = args.position
    if len(cur_pos) != 2:
        print("Position coordinate incorrect")
        sys.exit()

    obj = Chessercise()
    if type_of_piece == 'knight':
        print(obj.find_knight_possible_moves(cur_pos))
    elif type_of_piece == 'queen':
        print(obj.find_queen_possible_moves(cur_pos))
    elif type_of_piece == 'rook':
        print(obj.find_rook_possible_moves(cur_pos))
    else:
        print("Incorrect input for type of piece")
        sys.exit()

###################### PyLint Result ################################
#
# No config file found, using default configuration
# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
