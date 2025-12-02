def count_Primes_nums(n):
    '''Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.'''
    count = 0
    if n <= 2:
        return 0
    else:
        for num in range(2, n):
            if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
                count += 1
    return count

assert count_Primes_nums(5) == 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()