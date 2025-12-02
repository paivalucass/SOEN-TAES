def last_Digit(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n == 0:
        return 0
    return abs(n) % 10
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit(123), 3)

if __name__ == '__main__':
    unittest.main()