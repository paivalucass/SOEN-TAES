def cube_Sum(n):
  if not isinstance(n, int) or n < 0:
    raise ValueError("n should be a non-negative integer")

  sum = 0
  for i in range(2, n*2+2, 2):
    sum += i**3
  return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()