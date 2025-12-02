def is_polite(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2 * is_polite(n-1) + is_polite(n-2) + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()