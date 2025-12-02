def prime_fib(n):
    fib_seq = [1, 2]
    idx = 2
    while len(fib_seq) < n:
        next_fib = fib_seq[idx-1] + fib_seq[idx-2]
        fib_seq.append(next_fib)
        idx += 1
    primes = []
    for num in fib_seq:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes[n-1]
import unittest

class Test(unittest.TestCase):
    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()