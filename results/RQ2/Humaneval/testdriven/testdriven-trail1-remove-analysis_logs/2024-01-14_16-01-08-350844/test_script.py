def compare(game_scores, guess_scores):
    if not game_scores or not guess_scores:
        return "Error: Arrays cannot be empty"
    if len(game_scores) != len(guess_scores):
        return "Error: Unequal array lengths"
    result = []
    for i in range(len(game_scores)):
        if not (isinstance(game_scores[i], int) and isinstance(guess_scores[i], int)):
            return "Error: Arrays should only contain numerical values"
        if game_scores[i] == guess_scores[i]:
            result.append(0)
        else:
            result.append(abs(game_scores[i] - guess_scores[i]))
    return result
import unittest

class Test(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])

if __name__ == '__main__':
    unittest.main()