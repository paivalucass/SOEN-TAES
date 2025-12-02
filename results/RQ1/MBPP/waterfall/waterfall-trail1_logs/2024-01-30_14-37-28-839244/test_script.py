def first_Digit(n):
    if isinstance(n, int) or isinstance(n, float):
        n = abs(n)
        while n >= 10:
            n = n // 10
        return n
    else:
        return "Invalid input: Please enter a valid integer or float number"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_Digit(123), 1)

if __name__ == '__main__':
    unittest.main()