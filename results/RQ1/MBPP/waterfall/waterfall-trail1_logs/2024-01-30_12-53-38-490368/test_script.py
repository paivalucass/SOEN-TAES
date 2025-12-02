def even_Power_Sum(n):
  if not isinstance(n, int) or n <= 0:
    raise ValueError("Input n must be a positive integer")
  return sum([i**5 for i in range(2, 2*n+1, 2)])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()