def sum_to_n(n: int):
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    return n*(n+1)//2 # Using the formula for sum of first n natural numbers

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Input is a small value of n",
      "Input Data": "n=1",
      "Expected Output": "1"
    },
    {
      "Test Title": "Input is a large value of n",
      "Input Data": "n=100",
      "Expected Output": "5050"
    },
    {
      "Test Title": "Input is a negative value of n",
      "Input Data": "n=-5",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Input is a zero value of n",
      "Input Data": "n=0",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

if __name__ == '__main__':
    unittest.main()