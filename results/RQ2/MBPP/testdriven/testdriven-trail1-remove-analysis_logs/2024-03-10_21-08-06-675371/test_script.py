def is_octagonal(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Invalid input"
    else:
        return n * (3 * n - 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()