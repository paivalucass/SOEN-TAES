def is_perfect_square(n):
    if not isinstance(n, int):
        return "Error"
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    
    left = 1
    right = n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return True
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Positive Non-perfect Square",
      "Input Data": "n=10",
      "Expected Output": "False"
    },
    {
      "Test Title": "Negative Non-perfect Square",
      "Input Data": "n=-16",
      "Expected Output": "False"
    },
    {
      "Test Title": "Large Non-perfect Square",
      "Input Data": "n=1000000",
      "Expected Output": "False"
    },
    {
      "Test Title": "Non-Number Input",
      "Input Data": "n='abc'",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Out of Range Input",
      "Input Data": "n=1.7976931348623157e+308",
      "Expected Output": "Error"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_perfect_square(10), False)

if __name__ == '__main__':
    unittest.main()