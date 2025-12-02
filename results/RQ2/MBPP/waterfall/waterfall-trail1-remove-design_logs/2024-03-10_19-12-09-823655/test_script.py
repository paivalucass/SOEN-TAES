def square_Sum(n):
  if not isinstance(n, int) or n <= 0:
      return "Invalid input. Please enter a positive integer."

  total_sum = 0
  for num in range(1, (n*2)+1):
      if num % 2 == 0:
          total_sum += num ** 2
  
  return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()