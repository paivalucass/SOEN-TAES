def divisor(n):
    '''Write a python function to find the number of divisors of a given integer.
    assert divisor(15) == 4'''
    
    # Check if the input integer is positive
    if n <= 0:
        return "Error: Input integer must be a positive number."
    
    # Count the number of divisors
    num_divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            num_divisors += 2 if i * i != n else 1
    
    return num_divisors
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()