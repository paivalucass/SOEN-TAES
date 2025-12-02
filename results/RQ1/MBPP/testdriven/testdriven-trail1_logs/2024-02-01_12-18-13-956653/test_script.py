def next_Perfect_Square(N):
    if not isinstance(N, (int, float)) or N < 0:
        return "Invalid input. Please provide a valid positive number."

    sqrt = int(N ** 0.5) + 1
    return sqrt * sqrt
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()