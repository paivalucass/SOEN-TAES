def count_up_to(n):
    primes = []
    is_prime = [True] * (n + 1)
    for num in range(2, n):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, n, num):
                is_prime[multiple] = False
    return primes
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