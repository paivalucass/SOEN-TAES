def next_Perfect_Square(N):
    if type(N) != int or N <= 0:
        return "Input must be a positive integer"

    next_square_root = int(N ** 0.5) + 1
    next_perfect_square = next_square_root ** 2
    return next_perfect_square
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()