def prime_num(num):
    '''Write a function to check if the given integer is a prime number.'''
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function with various input values including prime and non-prime numbers
assert prime_num(13)==True
assert prime_num(15)==False
assert prime_num(2)==True
assert prime_num(1)==False

# Check for edge cases like negative numbers and zero
assert prime_num(-5)==False
assert prime_num(0)==False
import unittest

class Test(unittest.TestCase):
    def test_prime_num(self):
        self.assertEqual(prime_num(13), True)

if __name__ == '__main__':
    unittest.main()