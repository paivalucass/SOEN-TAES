def sum_of_digits_of_largest_prime(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(lst):
        return [num for num in lst if is_prime(num)]

    def get_largest_prime(lst):
        primes = get_primes(lst)
        if len(primes) == 0:
            return 0
        primes.sort(reverse=True)
        return primes[0]

    if len(lst) == 0 or not any(is_prime(num) for num in lst):
        return 0

    largest_prime = get_largest_prime(lst)
    return sum(int(digit) for digit in str(largest_prime))
import unittest

class Test(unittest.TestCase):
    def test_largest_prime_sum(self):
        self.assertEqual(largest_prime_sum([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)
        self.assertEqual(largest_prime_sum([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)
        self.assertEqual(largest_prime_sum([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)
        self.assertEqual(largest_prime_sum([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)
        self.assertEqual(largest_prime_sum([0,81,12,3,1,21]), 3)
        self.assertEqual(largest_prime_sum([0,8,1,2,1,7]), 7)

if __name__ == '__main__':
    unittest.main()