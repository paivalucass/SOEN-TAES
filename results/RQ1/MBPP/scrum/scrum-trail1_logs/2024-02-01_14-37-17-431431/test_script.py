def amicable_numbers_sum(limit):
    def sum_of_divisors(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum

    amicable_sum = 0
    for a in range(1, limit+1):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_sum += a

    return amicable_sum

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test with limit = 1000",
      "Input Data": "limit=1000",
      "Expected Output": 504
    },
    {
      "Test Title": "Test with limit = 999",
      "Input Data": "limit=999",
      "Expected Output": 504
    },
    {
      "Test Title": "Test with limit = 1001",
      "Input Data": "limit=1001",
      "Expected Output": 504
    },
    {
      "Test Title": "Test with limit = 1",
      "Input Data": "limit=1",
      "Expected Output": 0
    },
    {
      "Test Title": "Test with limit = -1",
      "Input Data": "limit=-1",
      "Expected Output": 0
    },
    {
      "Test Title": "Test with limit = 1000000",
      "Input Data": "limit=1000000",
      "Expected Output": 504
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()