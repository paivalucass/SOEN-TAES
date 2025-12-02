def newman_prime(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"

    if n == 1:
        return 2

    primes = [2, 3]
    num = 5
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2

    return primes[n-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()