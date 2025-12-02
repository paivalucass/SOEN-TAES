def sum(a, b):
  '''Write a python function to find the sum of common divisors of two given numbers.'''
  if not isinstance(a, int) or not isinstance(b, int) or a <= 0 or b <= 0:
    return "Error: Input parameters 'a' and 'b' must be positive integers"
  
  common_divisors = []
  limit = min(a, b)
  for i in range(1, limit + 1):
    if a % i == 0 and b % i == 0:
      common_divisors.append(i)
  
  return sum(common_divisors)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(10, 15), 6)

if __name__ == '__main__':
    unittest.main()