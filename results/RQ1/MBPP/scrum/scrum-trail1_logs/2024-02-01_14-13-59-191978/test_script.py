def is_octagonal(n):
    octagonal_number = 3 * n**2 - 2 * n
    return octagonal_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()