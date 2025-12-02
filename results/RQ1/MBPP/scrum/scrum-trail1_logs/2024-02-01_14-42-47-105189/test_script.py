def hexagonal_num(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    # Calculate the nth hexagonal number using the formula: 2*n**2 - n
    return 2 * n**2 - n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()