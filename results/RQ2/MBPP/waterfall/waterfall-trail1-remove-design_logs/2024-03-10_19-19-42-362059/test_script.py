def last_Digit_Factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input value n must be a non-negative integer")
    if n == 0:
        return 1

    result = 1
    for i in range(1, n+1):
        result *= i
    return result % 10
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()