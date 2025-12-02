def first_Digit(n):
    if type(n) in [int, float]:
        n = abs(n)
        while n >= 10:
            n = n // 10
        return n
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()