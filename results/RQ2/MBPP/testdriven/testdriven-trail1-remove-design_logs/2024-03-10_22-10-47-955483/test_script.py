def first_Digit(num):
    if not isinstance(num, int):
        raise ValueError("Input must be a number")
    if num < 0:
        raise ValueError("Input must be a positive number")

    while num >= 10:
        num = num // 10
    return abs(num)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()