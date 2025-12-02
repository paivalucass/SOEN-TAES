def last_Digit_Factorial(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input: n must be a positive integer"
    result = 1
    for i in range(1, n+1):
        result = (result * i) % 10
    return result
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()