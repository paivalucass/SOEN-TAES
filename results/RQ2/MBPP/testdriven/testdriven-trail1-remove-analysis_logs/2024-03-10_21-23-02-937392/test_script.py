def last_Digit_Factorial(n):
    '''Write a python function to find the last digit in factorial of a given number.'''
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        return factorial % 10

assert last_Digit_Factorial(4) == 4
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()