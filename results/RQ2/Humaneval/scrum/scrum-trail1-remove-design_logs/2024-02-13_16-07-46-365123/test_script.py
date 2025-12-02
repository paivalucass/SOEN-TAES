def largest_prime_factor(n: int):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_factors(num):
        factors = []
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                factors.append(divisor)
                num = num / divisor
            divisor += 1
        return factors

    factors = prime_factors(n)
    prime_factors_list = [factor for factor in factors if is_prime(factor)]
    return max(prime_factors_list) if prime_factors_list else "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()