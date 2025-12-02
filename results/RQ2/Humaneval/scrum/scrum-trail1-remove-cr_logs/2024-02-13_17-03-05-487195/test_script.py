def is_multiply_prime(a):
    if a > 99:
        return "Error: Input number must be less than or equal to 99."

    def sieve(n):
        primes = []
        sieve = [True] * (n + 1)
        for p in range(2, n + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return primes

    primes = sieve(a)
    if len(primes) < 3:
        return False
    else:
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                for k in range(j + 1, len(primes)):
                    if primes[i] * primes[j] * primes[k] == a:
                        return True
        return False

# Test cases
print(is_multiply_prime(30))
print(is_multiply_prime(99))
print(is_multiply_prime(1))
print(is_multiply_prime(0))
print(is_multiply_prime(101))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()