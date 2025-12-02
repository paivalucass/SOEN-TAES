def square_Sum(n):
  if n <= 0:
    return 0
  
  odd_number = 1
  result = 0
  for _ in range(n):
    result += (odd_number ** 2)
    odd_number += 2
  
  return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()