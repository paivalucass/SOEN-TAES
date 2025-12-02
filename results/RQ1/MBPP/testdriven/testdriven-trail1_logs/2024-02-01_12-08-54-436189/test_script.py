def hexagonal_num(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input, n must be a positive integer"
    return 2 * n**2 - n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()