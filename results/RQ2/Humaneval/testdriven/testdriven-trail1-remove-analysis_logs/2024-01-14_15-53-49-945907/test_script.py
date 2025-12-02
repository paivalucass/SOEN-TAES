def find_largest_prime_and_sum_of_digits(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(num):
        return sum([int(x) for x in str(num)])
    
    primes = [x for x in lst if is_prime(x)]
    max_prime = max(primes)
    return sum_of_digits(max_prime)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(largest_prime_sum([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]), 10)

    def test2(self):
        self.assertEqual(largest_prime_sum([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]), 25)

    def test3(self):
        self.assertEqual(largest_prime_sum([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]), 13)

    def test4(self):
        self.assertEqual(largest_prime_sum([0,724,32,71,99,32,6,0,5,91,83,0,5,6]), 11)

    def test5(self):
        self.assertEqual(largest_prime_sum([0,81,12,3,1,21]), 3)

    def test6(self):
        self.assertEqual(largest_prime_sum([0,8,1,2,1,7]), 7)

if __name__ == '__main__':
    unittest.main()