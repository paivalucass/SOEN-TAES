def find_power_of_2(n):
    if isinstance(n, int):
        return 2 ** n
    else:
        return 1

def next_power_of_2(n):
    if n <= 0:
        return 1
    else:
        power = 1
        while power < n:
            power *= 2
        return power

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Check smallest power of 2 for 0",
      "Input Data": "n=0",
      "Expected Output": "1"
    },
    {
      "Test Title": "Check smallest power of 2 for positive integer",
      "Input Data": "n=5",
      "Expected Output": "8"
    },
    {
      "Test Title": "Check smallest power of 2 for large integer",
      "Input Data": "n=1000",
      "Expected Output": "1024"
    },
    {
      "Test Title": "Check smallest power of 2 for negative integer",
      "Input Data": "n=-5",
      "Expected Output": "1"
    },
    {
      "Test Title": "Check smallest power of 2 for non-integer input",
      "Input Data": "n='abc'",
      "Expected Output": "1"
    },
    {
      "Test Title": "Check smallest power of 2 for n=1",
      "Input Data": "n=1",
      "Expected Output": "1"
    },
    {
      "Test Title": "Check smallest power of 2 for n=2",
      "Input Data": "n=2",
      "Expected Output": "2"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()