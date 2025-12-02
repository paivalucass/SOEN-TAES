def left_rotate(n, d):
    result = (n << d) | (n >> (32 - d)) 
    return result 

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Positive Number Rotation",
      "Input Data": "n=16, d=2",
      "Expected Output": "64"
    },
    {
      "Test Title": "Negative Number Rotation",
      "Input Data": "n=-16, d=3",
      "Expected Output": "-128"
    },
    {
      "Test Title": "Boundary Case Rotation",
      "Input Data": "n=1, d=31",
      "Expected Output": "2147483648"
    },
    {
      "Test Title": "Zero Value Rotation",
      "Input Data": "n=0, d=5",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative Value Rotation",
      "Input Data": "n=16, d=-2",
      "Expected Output": "1"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_rotate(16,2), 64)

if __name__ == '__main__':
    unittest.main()