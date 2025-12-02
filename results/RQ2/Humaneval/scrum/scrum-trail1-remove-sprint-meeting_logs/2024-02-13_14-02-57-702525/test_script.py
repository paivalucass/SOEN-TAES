def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def triangle_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return -1  # Invalid triangle

    if is_valid_triangle(a, b, c):
        area = calculate_area(a, b, c)
        return round(area, 2)  # Return the calculated area rounded to 2 decimal points
    else:
        return -1  # Invalid triangle

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Triangle Sides - Equilateral",
      "Input Data": "a=5, b=5, c=5",
      "Expected Output": "10.83"
    },
    {
      "Test Title": "Valid Triangle Sides - Isosceles",
      "Input Data": "a=3, b=3, c=4",
      "Expected Output": "4.47"
    },
    {
      "Test Title": "Valid Triangle Sides - Scalene",
      "Input Data": "a=3, b=4, c=5",
      "Expected Output": "6.00"
    },
    {
      "Test Title": "Invalid Triangle Sides - Negative Numbers",
      "Input Data": "a=-1, b=2, c=10",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Invalid Triangle Sides - Zero",
      "Input Data": "a=0, b=0, c=0",
      "Expected Output": "-1"
    },
    {
      "Test Title": "Invalid Triangle Sides - Non-Numeric Inputs",
      "Input Data": "a='abc', b='def', c='ghi'",
      "Expected Output": "-1"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_triangle_area_valid(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_triangle_area_invalid(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

if __name__ == '__main__':
    unittest.main()