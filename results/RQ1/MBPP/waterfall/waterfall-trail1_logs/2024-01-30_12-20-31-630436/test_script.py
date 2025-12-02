def is_octagonal(n):
    if type(n) != int or n < 0:
        return "Invalid input"

    octagonal_number = n * (3 * n - 2)
    return octagonal_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()