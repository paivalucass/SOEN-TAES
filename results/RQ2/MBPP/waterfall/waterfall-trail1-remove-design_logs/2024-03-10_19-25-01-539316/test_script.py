def jacobsthal_num(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            c = b
            b = b + 2 * a
            a = c
        return b

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Test",
      "Input Data": "parameter1=5",
      "Expected Output": "11"
    },
    {
      "Test Title": "Boundary Input Test",
      "Input Data": "parameter1=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large Input Test",
      "Input Data": "parameter1=15",
      "Expected Output": "2731"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()