def amicable_numbers_sum(limit):
    # Function to calculate the sum of all amicable numbers from 1 to a specified number
    def sum_of_divisors(n):
        # Function to calculate the sum of proper divisors of a number
        result = 0
        for i in range(1, n):
            if n % i == 0:
                result += i
        return result

    # Calculate amicable sum
    amicable_sum = 0
    for i in range(1, limit+1):
        partner = sum_of_divisors(i)
        if i != partner and sum_of_divisors(partner) == i:
            amicable_sum += i

    return amicable_sum

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Test",
      "Input Data": "limit=220",
      "Expected Output": "284"
    },
    {
      "Test Title": "Invalid Input Test",
      "Input Data": "limit=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Boundary Input Test",
      "Input Data": "limit=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Edge Case Test",
      "Input Data": "limit=-100",
      "Expected Output": "0"
    },
    {
      "Test Title": "Additional Edge Case Test",
      "Input Data": "limit=1000",
      "Expected Output": "504"
    },
    {
      "Test Title": "Detailed Output Test",
      "Input Data": "limit=500",
      "Expected Output": "504"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()