def is_Even(n):
    try:
        return n % 2 == 0
    except TypeError:
        raise TypeError("Input must be a number")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Even(1), False)

if __name__ == '__main__':
    unittest.main()