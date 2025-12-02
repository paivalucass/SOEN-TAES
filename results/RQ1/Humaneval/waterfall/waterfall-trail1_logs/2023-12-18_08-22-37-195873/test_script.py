def count_up_to(n):
    primes = []
    if n <= 1:
        return primes

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)

    return primes[:n]
import unittest

class Test(unittest.TestCase):
    def test_count_up_to(self):
        self.assertEqual(count_up_to(5), [2, 3])
        self.assertEqual(count_up_to(11), [2, 3, 5, 7])
        self.assertEqual(count_up_to(0), [])
        self.assertEqual(count_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(count_up_to(1), [])
        self.assertEqual(count_up_to(18), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()