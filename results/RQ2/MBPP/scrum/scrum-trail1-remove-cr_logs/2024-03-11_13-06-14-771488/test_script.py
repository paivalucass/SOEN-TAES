def sum_div(number):
    sum_of_divisors = 0
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors

# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "valid input test",
      "Input Data": "number=8",
      "Expected Output": "7"
    },
    {
      "Test Title": "edge case test",
      "Input Data": "number=1",
      "Expected Output": "1"
    },
    {
      "Test Title": "large number test",
      "Input Data": "number=1000000",
      "Expected Output": "1344000"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()