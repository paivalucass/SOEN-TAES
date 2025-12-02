def prime_factorization(num):
    if num <= 1:
        return []
    prime_factors = []
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor:
            divisor += 1
        else:
            num //= divisor
            prime_factors.append(divisor)
    if num > 1:
        prime_factors.append(num)
    return prime_factors

def is_multiply_prime(a):
    if a <= 1:
        return False
    factors = prime_factorization(a)
    return len(factors) == 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()