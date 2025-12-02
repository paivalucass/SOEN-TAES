def factorial(n):
    if n < 0:
        return None  # handle negative numbers
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def last_digit(n):
    return n % 10

def last_Digit_Factorial(n):
    if type(n) != int or n < 0:
        return None  # handle non-integer and negative inputs
    fact = factorial(n)
    if fact is None:
        return None
    return last_digit(fact)  # find last digit in factorial

# Test cases
assert last_Digit_Factorial(4) == 4
assert last_Digit_Factorial(0) == 1
assert last_Digit_Factorial(1) == 1
assert last_Digit_Factorial(5) == 0
assert last_Digit_Factorial(10) == 0
assert last_Digit_Factorial(15) == 0
assert last_Digit_Factorial(20) == 0
assert last_Digit_Factorial(-5) == None
assert last_Digit_Factorial(3.5) == None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit_Factorial(4), 4)

if __name__ == '__main__':
    unittest.main()