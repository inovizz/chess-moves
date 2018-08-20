"""Test case for chess.py."""

import unittest
from chess import Chessercise


class ChessTestCase(unittest.TestCase):
    """ChessTestCase class for unit testing Chessercise class."""
    def setUp(self):
        """Setup() method."""
        self.obj = Chessercise()

    def test_find_coordinates(self):
        """Test case for find coordinates function."""
        # "D2" is algebraic notation of cooridnate (3,1)
        input1 = 'd2'
        res = self.obj.find_coordinates(input1)
        self.assertEqual((3, 1), res)

        input2 = 'd9'
        res = self.obj.find_coordinates(input2)
        self.assertNotEqual(res, (3, 1))

    def test_get_algebraic_coordinate(self):
        """Test case for get algebraic coordinate function."""
        # (3,1) are the coordinates for algebraic notation d2
        input1 = [3, 1]
        res = self.obj.get_algebraic_coordinate(input1[0], input1[1])
        self.assertEqual('d2', res)

        input2 = [9, 9]
        res = self.obj.get_algebraic_coordinate(input2[0], input2[1])
        self.assertNotEqual(res, (9, 9))

    def test_find_queen_possible_moves(self):
        """Test case for find possible queen moves function."""
        input1 = 'g5'
        res = self.obj.find_queen_possible_moves(input1)
        self.assertEqual(res, 'h6, h4, f6, e7, d8, f4, e3, d2, c1, a5, b5, '
                              'c5, d5, e5, f5, h5, g1, g2, g3, g4, g6, g7, g8')

    def test_find_knight_possible_moves(self):
        """Test case for find possible knight moves function."""
        input1 = 'g4'
        res = self.obj.find_knight_possible_moves(input1)
        self.assertEqual(res, 'h6, h2, f6, f2, e5, e3')
        input2 = 'a1'
        res = self.obj.find_knight_possible_moves(input2)
        self.assertEqual(res, 'b3, c2')
        input3 = 'a8'
        res = self.obj.find_knight_possible_moves(input3)
        self.assertEqual(res, 'b6, c7')
        input4 = 'h1'
        res = self.obj.find_knight_possible_moves(input4)
        self.assertEqual(res, 'g3, f2')
        input5 = 'h8'
        res = self.obj.find_knight_possible_moves(input5)
        self.assertEqual(res, 'g6, f7')

    def test_find_rook_possible_moves(self):
        """Test case for find rook possible moves function."""
        input1 = 'e4'
        res = self.obj.find_rook_possible_moves(input1)
        self.assertEqual(
            res, 'a4, b4, c4, d4, f4, g4, h4, e1, e2, e3, e5, e6, e7, e8')

###################### Test Coverage ####################################
# nosetests test_chess.py - -with-coverage
# .....
# Name       Stmts   Miss  Cover   Missing
# ----------------------------------------
# chess.py     103     18    83 % 162-186
# ----------------------------------------------------------------------
# Ran 5 tests in 0.010s
