def newman_prime(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    primes = [2, 3, 5, 11, 17, 41, 197, 199, 487, 1013, 5653, 6481, 107089, 936197, 723227, 1855075, 2147483647, 514229, 433494437]
    if n > len(primes):
        return "Invalid input"
    return primes[n-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()