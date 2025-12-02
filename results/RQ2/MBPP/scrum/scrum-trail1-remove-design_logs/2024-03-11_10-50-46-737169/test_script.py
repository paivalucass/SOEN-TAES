def last_Digit_Factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Input must be a non-negative integer"
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial % 10
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()