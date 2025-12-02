def count_Primes_nums(n):
    if n < 3:
        return 0

    primes = [True] * n
    primes[0:2] = [False, False]

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * ((n-1-i*i)//i + 1)

    return sum(primes[2:])

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()