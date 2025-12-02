def divisor(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("Input must be a non-negative integer")

  count = 0
  for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
      count += 2 if i * i != n else 1

  return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()