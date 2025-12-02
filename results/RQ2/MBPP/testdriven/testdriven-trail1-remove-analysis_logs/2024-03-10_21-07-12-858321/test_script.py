def is_not_prime(num):
    '''Write a python function to identify non-prime numbers.'''
    if num <= 1:
        return True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

assert is_not_prime(2) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_not_prime(2), False)

if __name__ == '__main__':
    unittest.main()