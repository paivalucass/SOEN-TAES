def cube_sum(n):
  sum = 0
  for i in range(2, 2*n+1, 2):
    sum += i**3
  return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()