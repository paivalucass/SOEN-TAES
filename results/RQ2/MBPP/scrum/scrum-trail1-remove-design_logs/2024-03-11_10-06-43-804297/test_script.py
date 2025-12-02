def amicable_numbers_sum(limit):
    result = 0
    for num in range(1, limit):
        if is_amicable(num):
            result += num
    return result

def is_amicable(num):
    sum_divisors = sum(get_divisors(num))
    if sum_divisors == num:
        return False
    return sum(get_divisors(sum_divisors)) == num

def get_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

# Test Cases:
{
  "requirement analysis": "Comprehensive unit tests should be implemented to validate the functionality of the function for summing amicable numbers, including edge cases and different input ranges to ensure accuracy and robustness of the calculation.",
  "test_cases": [
    {
      "Test Title": "Valid input range",
      "Input Data": "limit=100",
      "Expected Output": "504"
    },
    {
      "Test Title": "Boundary input range",
      "Input Data": "limit=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large input range",
      "Input Data": "limit=10000",
      "Expected Output": "31626"
    },
    {
      "Test Title": "Negative input range",
      "Input Data": "limit=-100",
      "Expected Output": "0"
    },
    {
      "Test Title": "Zero input range",
      "Input Data": "limit=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Invalid input data",
      "Input Data": "limit='abc'",
      "Expected Output": "Invalid input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()