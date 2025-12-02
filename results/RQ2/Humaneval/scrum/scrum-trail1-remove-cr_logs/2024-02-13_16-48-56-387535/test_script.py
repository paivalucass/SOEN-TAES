def largest_divisor(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
        
    if n <= 0:
        return None

    largest = 1
    for i in range(2, n):
        if n % i == 0:
            largest = i

    return largest

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Test",
      "Input Data": "parameter1=15",
      "Expected Output": "5"
    },
    {
      "Test Title": "Zero Input Test",
      "Input Data": "parameter1=0",
      "Expected Output": "None"
    },
    {
      "Test Title": "Negative Input Test",
      "Input Data": "parameter1=-15",
      "Expected Output": "None"
    },
    {
      "Test Title": "Large Input Test",
      "Input Data": "parameter1=999999",
      "Expected Output": "499999"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)

if __name__ == '__main__':
    unittest.main()