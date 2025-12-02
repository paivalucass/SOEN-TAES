def is_polite(n):
    result = 0
    for i in range(1, n + 1):
        result += 2 ** (i - 1)
    return result - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()