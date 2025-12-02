def count_Primes_nums(n):
  if not isinstance(n, int) or n < 0:
    return 'Invalid input'
  if n < 2:
    return 0
  primes = [True] * n
  primes[0], primes[1] = False, False
  for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
      primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
  return sum(primes)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Primes_nums(5), 2)

if __name__ == '__main__':
    unittest.main()