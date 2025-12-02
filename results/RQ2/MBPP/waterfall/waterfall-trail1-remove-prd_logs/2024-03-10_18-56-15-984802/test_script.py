def is_polite(n):
    if n > 0:
        return n + 3
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()