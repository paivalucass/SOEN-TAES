def is_woodall(x):
    if not isinstance(x, int) or x <= 0:
        raise ValueError("Input x must be a positive integer")

    result = x * (2 ** x - 1)
    return result == x * 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_woodall(383), True)

if __name__ == '__main__':
    unittest.main()