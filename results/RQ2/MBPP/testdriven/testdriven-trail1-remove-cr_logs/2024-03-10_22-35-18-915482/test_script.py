def count_Primes_nums(n):
    def sieve_of_eratosthenes(limit):
        primes = []
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for num in range(2, limit):
            if is_prime[num]:
                primes.append(num)
                for multiple in range(num * num, limit + 1, num):
                    is_prime[multiple] = False
        return len(primes)

    if n < 2:
        return 0
    else:
        return sieve_of_eratosthenes(n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()