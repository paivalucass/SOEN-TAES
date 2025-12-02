def starts_one_ends(n):
    count = 0
    if n == 1:
        count = 1
    else:
        count = 18 * 10 ** (n-2)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(starts_one_ends(2), 19)
        self.assertEqual(starts_one_ends(3), 271)

if __name__ == '__main__':
    unittest.main()