def prime_num(num):
    '''Function to check if the given integer is a prime number.'''
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_prime_num(self):
        self.assertEqual(prime_num(13), True)

if __name__ == '__main__':
    unittest.main()