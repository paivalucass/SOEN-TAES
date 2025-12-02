def is_prime(num: int) -> bool:
    '''Write a function to check if the given integer is a prime number.'''
    if num <= 1:
        return False  # input validation to ensure the input integer is greater than 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # efficient Sieve of Eratosthenes algorithm to check for prime numbers
    return True

# test assertion:
assert is_prime(13) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_num(13), True)

if __name__ == '__main__':
    unittest.main()