import unittest
from boggle_solver import Boggle

class TestBoggleSolver(unittest.TestCase):
    
    # Test for a normal 3x3 grid with a dictionary
    def test_3x3_grid(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["ABC", "AEI", "CFI"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["ABC", "AEI", "CFI"]  # Adjusted expected output
        self.assertEqual(sorted(solution), sorted(expected))

    # Test for an empty grid
    def test_empty_grid(self):
        grid = [[]]
        dictionary = ["ANY", "WORD"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        self.assertEqual(solution, [])

    # Test for a 1x1 grid with no valid words
    def test_1x1_grid(self):
        grid = [["A"]]
        dictionary = ["B", "C"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        self.assertEqual(solution, [])

    # Test for a 4x4 grid with diagonal words
    def test_4x4_grid_diagonal(self):
        grid = [["A", "B", "C", "D"], ["E", "F", "G", "H"], ["I", "J", "K", "L"], ["M", "N", "O", "P"]]
        dictionary = ["AFKP", "BFJN", "DGJM"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["AFKP", "BFJN", "DGJM"]  # Adjusted expected output
        self.assertEqual(sorted(solution), sorted(expected))

    # Test for an empty dictionary
    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        self.assertEqual(solution, [])

    # Test for grids with 'Qu' and 'St'
    def test_qu_and_st(self):
        grid = [["Q", "U", "A"], ["S", "T", "E"], ["T", "R", "S"]]
        dictionary = ["QUEST", "STAR", "STE"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["QUEST", "STE"]
        self.assertEqual(sorted(solution), sorted(expected))

if __name__ == '__main__':
    unittest.main()
