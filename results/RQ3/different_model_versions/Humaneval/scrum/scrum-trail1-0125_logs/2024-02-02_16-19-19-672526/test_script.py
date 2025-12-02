def is_multiply_prime(a):
    def generate_primes():
        primes = []
        for num in range(2, 100):
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                primes.append(num)
        return primes
    
    primes = generate_primes()
    
    if a <= 0 or a >= 100:
        return False
    
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            for k in range(j + 1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()