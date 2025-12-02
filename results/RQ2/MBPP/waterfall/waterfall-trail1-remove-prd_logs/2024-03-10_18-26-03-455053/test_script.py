def is_octagonal(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input n must be a positive integer")

    nth_octagonal_number = 3 * n**2 - 2 * n
    return nth_octagonal_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()