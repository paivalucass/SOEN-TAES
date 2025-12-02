def starts_one_ends(n):
    count = 0
    if n < 1:
        return count
    count = 2 * 9 * 10 ** (n-2) + 10 ** (n-1) - 9 ** (n-1)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 11)
        self.assertEqual(starts_one_ends(3), 111)

if __name__ == '__main__':
    unittest.main()