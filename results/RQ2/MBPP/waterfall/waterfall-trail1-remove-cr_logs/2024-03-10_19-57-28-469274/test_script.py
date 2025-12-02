def next_Perfect_Square(N):
    if not isinstance(N, int) or N < 0:
        raise ValueError("Invalid input: N must be a non-negative integer")

    next_square = (int(N ** 0.5) + 1) ** 2
    return next_square
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()