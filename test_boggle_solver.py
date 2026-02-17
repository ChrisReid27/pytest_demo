# Christopher Reid SID: 03122717

import unittest
import sys

sys.path.append("/home/codio/workspace/") #have to tell the unittest the PATH to find boggle_solver.py and the Boggle Class

from boggle_solver import Boggle

class TestBoggle(unittest.TestCase):
    def setUp(self):
        # Default dictionary for general tests
        self.common_dict = ["rat", "stop", "field", "qua", "quasta", "ten", "abc", "eae"]

    def test_frame_1_min_length_fail(self):
        """Frame 1: Word < 3 letters (ab) should not be in solutions."""
        grid = [["A", "B"], ["C", "D"]]
        game = Boggle(grid, ["ab"])
        self.assertEqual(game.getSolution(), [])

    def test_frame_2_standard_3_letters(self):
        """Frame 2: Standard 3-letter word (rat)."""
        grid = [["R", "A", "T"], ["X", "X", "X"], ["X", "X", "X"]]
        game = Boggle(grid, ["rat"])
        self.assertIn("rat", game.getSolution())

    def test_frame_3_qu_tile(self):
        """Frame 3: 'Qu' (2) + 'A' (1) = 3 letters (Valid)."""
        grid = [["Qu", "A"], ["X", "X"]]
        game = Boggle(grid, ["qua"])
        self.assertIn("qua", game.getSolution())

    def test_frame_4_st_tile(self):
        """Frame 4: 'St' (2) + 'O' (1) + 'P' (1) = 4 letters."""
        grid = [["St", "O", "P"], ["X", "X", "X"]]
        game = Boggle(grid, ["stop"])
        self.assertIn("stop", game.getSolution())

    def test_frame_5_ie_tile(self):
        """Frame 5: 'F' + 'Ie' + 'L' + 'D' = 5 letters."""
        grid = [["F", "Ie", "L", "D"], ["X", "X", "X", "X"]]
        game = Boggle(grid, ["field"])
        self.assertIn("field", game.getSolution())

    def test_frame_6_cube_reuse_fail(self):
        """Frame 6: Cannot use the same 'E' cube twice for 'EAE'."""
        grid = [["E", "A"], ["X", "X"]]
        game = Boggle(grid, ["eae"])
        self.assertEqual(game.getSolution(), [])

    def test_frame_7_diagonal_connectivity(self):
        """Frame 7: A->B->C connected diagonally."""
        grid = [["A", "X"], ["X", "B"], ["C", "X"]]
        game = Boggle(grid, ["abc"])
        self.assertIn("abc", game.getSolution())

    def test_frame_8_case_insensitivity(self):
        """Frame 8: Grid lowercase, Dictionary uppercase."""
        grid = [["t", "e", "n"], ["X", "X", "X"]]
        game = Boggle(grid, ["TEN"])
        self.assertIn("ten", game.getSolution())

    def test_frame_9_overlapping_special_tiles(self):
        """Frame 9: 'Qu' + 'A' + 'St' + 'A' = 6 letters."""
        grid = [["Qu", "St"], ["A", "A"]]
        game = Boggle(grid, ["quasta"])
        self.assertIn("quasta", game.getSolution())

    def test_frame_10_disconnected_path(self):
        """Frame 10: Word exists in tiles but they are not adjacent."""
        grid = [["A", "B", "C"], ["X", "X", "X"], ["D", "E", "F"]]
        game = Boggle(grid, ["ade"])
        self.assertEqual(game.getSolution(), [])

if __name__ == "__main__":
    unittest.main()

# argv=['first-arg-is-ignored'], exit=False