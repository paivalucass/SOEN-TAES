def input_validation(game, guess):
    if len(game) != len(guess):
        raise ValueError("Length of game and guess arrays should be equal")
    if not all(isinstance(x, (int, float)) for x in game):
        raise ValueError("All elements in the game array should be numeric")
    if not all(isinstance(x, (int, float)) for x in guess):
        raise ValueError("All elements in the guess array should be numeric")

def calculate_difference(game, guess):
    differences = []
    for i in range(len(game)):
        differences.append(abs(game[i] - guess[i]) if game[i] != guess[i] else 0)
    return differences

def compare(game, guess):
    input_validation(game, guess)
    return calculate_difference(game, guess)
import unittest

class Test(unittest.TestCase):
    def test_compare1(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])

    def test_compare2(self):
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])

if __name__ == '__main__':
    unittest.main()