def compare(game, guess):
    if len(game) != len(guess):
        raise ValueError("Input arrays must be of equal length")

    return [abs(game[i] - guess[i]) if game[i] != guess[i] else 0 for i in range(len(game))]
import unittest

class Test(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])

if __name__ == '__main__':
    unittest.main()