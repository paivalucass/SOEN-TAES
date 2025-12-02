def sum_div(number):
    if number <= 0:
        return "Input number should be a positive integer"
    elif number == 1:
        return 1
    else:
        divisors_sum = 1
        for i in range(2, int(number/2) + 1):
            if number % i == 0:
                divisors_sum += i
        return divisors_sum

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Handle edge cases",
      "Input Data": "parameter1=0, parameter1=1",
      "Expected Output": "Input number should be a positive integer"
    },
    {
      "Test Title": "Handle negative numbers",
      "Input Data": "parameter1=-5",
      "Expected Output": "Input number should be a positive integer"
    },
    {
      "Test Title": "Calculate sum of divisors",
      "Input Data": "parameter1=8, parameter1=100",
      "Expected Output": 7
    },
    {
      "Test Title": "Handle prime number",
      "Input Data": "parameter1=7, parameter1=17, parameter1=23",
      "Expected Output": 1
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()