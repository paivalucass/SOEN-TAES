def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n < 2:
        return []
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

import unittest

class Test(unittest.TestCase):
    def test_count_up_to(self):
        self.assertEqual(function_under_test(5), [2, 3])
        self.assertEqual(function_under_test(11), [2, 3, 5, 7])
        self.assertEqual(function_under_test(0), [])
        self.assertEqual(function_under_test(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(function_under_test(1), [])
        self.assertEqual(function_under_test(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()