def lateralsuface_cylinder(radius, height):
    if radius <= 0 or height <= 0:
        return "Invalid input"
    return 2 * math.pi * radius * height

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Positive Radius and Height",
      "Input Data": "r=10.5,h=5.2",
      "Expected Output": "329.868"
    },
    {
      "Test Title": "Negative Radius and Height",
      "Input Data": "r=-10.5,h=-5.2",
      "Expected Output": "Invalid input"
    },
    {
      "Test Title": "Zero Radius and Height",
      "Input Data": "r=0,h=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large Input Values",
      "Input Data": "r=1000.5,h=500.2",
      "Expected Output": "3148681"
    }
  ]
}
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.1592653589793, places=10)

if __name__ == '__main__':
    unittest.main()