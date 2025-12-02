def right_angle_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False  # Input validation for positive lengths
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return False  # Input validation for valid triangle lengths
    a_sq = a * a
    b_sq = b * b
    c_sq = c * c
    if (a_sq + b_sq == c_sq) or (a_sq + c_sq == b_sq) or (b_sq + c_sq == a_sq):
        return True  # Check for right-angled triangle using Pythagorean theorem
    else:
        return False

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Right-Angled Triangle",
      "Input Data": "a=3, b=4, c=5",
      "Expected Output": "True"
    },
    {
      "Test Title": "Invalid Triangle",
      "Input Data": "a=1, b=2, c=3",
      "Expected Output": "False"
    },
    {
      "Test Title": "Edge Case: All Sides are Zero",
      "Input Data": "a=0, b=0, c=0",
      "Expected Output": "False"
    },
    {
      "Test Title": "Edge Case: Large Input Values",
      "Input Data": "a=1000000, b=1000000, c=1414214",
      "Expected Output": "True"
    },
    {
      "Test Title": "Floating Point Numbers",
      "Input Data": "a=3.5, b=4, c=5.5",
      "Expected Output": "True"
    },
    {
      "Test Title": "Negative Input Values",
      "Input Data": "a=-3, b=-4, c=-5",
      "Expected Output": "False"
    },
    {
      "Test Title": "Non-Numeric Input Values",
      "Input Data": "a='abc', b='def', c='ghi'",
      "Expected Output": "Invalid Input"
    },
    {
      "Test Title": "Boundary Values: Maximum Possible Values",
      "Input Data": "a=2147483647, b=2147483647, c=2147483647",
      "Expected Output": "True"
    },
    {
      "Test Title": "Boundary Values: Minimum Possible Values",
      "Input Data": "a=1, b=1, c=1",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_right_angle_triangle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertFalse(right_angle_triangle(1, 2, 3))

if __name__ == '__main__':
    unittest.main()