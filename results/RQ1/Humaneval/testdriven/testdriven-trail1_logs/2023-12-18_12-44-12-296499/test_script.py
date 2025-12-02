def compare(game, guess):
    if not isinstance(game, list) or not isinstance(guess, list):
        return "Invalid input. Please provide valid arrays as input."

    if len(game) != len(guess):
        return "Length of input arrays does not match."

    if len(game) == 0 or len(guess) == 0:
        return []

    if not all(isinstance(x, (int, float)) for x in game) or not all(isinstance(y, (int, float)) for y in guess):
        return "Elements of input arrays should be numbers."

    result = [abs(game[i] - guess[i]) for i in range(len(game))]

    return result
import unittest

class Test(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])

if __name__ == '__main__':
    unittest.main()