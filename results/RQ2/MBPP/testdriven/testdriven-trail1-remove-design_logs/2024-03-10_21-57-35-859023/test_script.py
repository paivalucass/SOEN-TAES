def divisor(n):
    '''Write a python function to find the number of divisors of a given integer.
    assert divisor(15) == 4'''

    # Check for invalid input
    if type(n) != int or n < 1:
        return "Invalid Input"
    
    # Handle case where n is 1
    if n == 1:
        return 1
    
    # Count the divisors
    count = 2  # Accounting for 1 and n itself
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # If divisors are equal, count only once
            if i == (n // i):
                count += 1
            else:
                count += 2
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()