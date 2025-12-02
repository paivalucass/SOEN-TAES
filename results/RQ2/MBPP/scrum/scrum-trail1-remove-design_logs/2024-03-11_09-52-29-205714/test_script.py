def is_not_prime(n):
    '''Write a python function to identify non-prime numbers.'''
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

# Test cases
assert is_not_prime(2) == False
assert is_not_prime(4) == True
assert is_not_prime(5) == False
assert is_not_prime(17) == False
assert is_not_prime(27) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_not_prime(2), False)

if __name__ == '__main__':
    unittest.main()