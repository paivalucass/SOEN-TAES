def odd_num_sum(n):
  odd_sum = 0
  for i in range(1, 2*n+1, 2):
    odd_sum += i ** 4
  return odd_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()