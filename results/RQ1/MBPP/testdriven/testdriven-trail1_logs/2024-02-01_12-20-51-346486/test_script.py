def count_Primes_nums(n):
    '''Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
    assert count_Primes_nums(5) == 2'''
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n < 2:
        return 0

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1

    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()