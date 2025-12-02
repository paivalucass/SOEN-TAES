def prime_num(num):
    '''Function to check if the given integer is a prime number.'''
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True if num > 1 else False
import unittest

class Test(unittest.TestCase):
    def test_prime_num(self):
        self.assertTrue(prime_num(13))

if __name__ == '__main__':
    unittest.main()