def compare(game, guess):
    if not all(isinstance(x, (int, float)) for x in game) or not all(isinstance(x, (int, float)) for x in guess):
        raise ValueError("Inputs must be arrays of numbers")

    if len(game) != len(guess):
        raise ValueError("Input arrays must be of equal length")

    if len(game) == 0:
        return []

    result = []
    for i in range(len(game)):
        if not isinstance(game[i], (int, float)) or not isinstance(guess[i], (int, float)):
            raise ValueError("Inputs must be arrays of numbers")

        diff = abs(game[i] - guess[i])
        result.append(diff)

    return result
import unittest

class Test(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])

if __name__ == '__main__':
    unittest.main()