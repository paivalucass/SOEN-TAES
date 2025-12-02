def is_prime_number(num):
    '''Write a function to check if the given integer is a prime number.'''
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    assert is_prime_number(13) == True
    assert is_prime_number(0) == False
    assert is_prime_number(1) == False
    assert is_prime_number(-13) == False
except AssertionError:
    print("Test case failed")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_num(13), True)

if __name__ == '__main__':
    unittest.main()