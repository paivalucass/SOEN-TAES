def last_Digit_Factorial(n):
    try:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Input must be a positive integer")
        
        if n == 0:
            return 1
        
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        
        last_digit = factorial % 10
        return last_digit
    
    except ValueError as ve:
        print(ve)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()