def count_Set_Bits(n):
    count = 0
    if n < 0:
        return "Input should be a non-negative integer"
    while n:
        count += n & 1
        n >>= 1
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input - positive number",
      "Input Data": "parameter1=2",
      "Expected Output": "1"
    },
    {
      "Test Title": "Valid input - zero",
      "Input Data": "parameter1=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Valid input - negative number",
      "Input Data": "parameter1=-2",
      "Expected Output": "1"
    },
    {
      "Test Title": "Valid input - large positive number",
      "Input Data": "parameter1=2147483647",
      "Expected Output": "31"
    },
    {
      "Test Title": "Performance test - very large input value",
      "Input Data": "parameter1=9223372036854775807",
      "Expected Output": "63"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Set_Bits(2), 1)

if __name__ == '__main__':
    unittest.main()