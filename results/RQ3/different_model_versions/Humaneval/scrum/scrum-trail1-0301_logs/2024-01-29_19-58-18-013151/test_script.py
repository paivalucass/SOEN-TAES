def is_multiply_prime(a):
    def is_valid_input(prime_nums):
        if len(prime_nums) != 3 or not all(isinstance(num, int) and num > 1 for num in prime_nums):
            raise ValueError("Input must be a list of three prime numbers greater than 1.")
        return True
    
    def multiply_primes(prime_nums):
        return prime_nums[0] * prime_nums[1] * prime_nums[2]
    
    def get_primes(n):
        primes = []
        for num in range(2, n):
            prime = True
            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break
            if prime:
                primes.append(num)
        return primes
    
    prime_nums = get_primes(100)[:3]
    is_valid_input(prime_nums)
    multiplication_result = multiply_primes(prime_nums)
    return multiplication_result == a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)
        self.assertEqual(is_multiply_prime(24), False)
        self.assertEqual(is_multiply_prime(77), False)
        self.assertEqual(is_multiply_prime(9), False)

if __name__ == '__main__':
    unittest.main()