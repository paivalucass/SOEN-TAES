def is_not_prime(n):
    '''Write a python function to identify non-prime numbers.'''
    if not isinstance(n, int) or n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
# Test cases
assert is_not_prime(2) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_not_prime(2), False)

if __name__ == '__main__':
    unittest.main()