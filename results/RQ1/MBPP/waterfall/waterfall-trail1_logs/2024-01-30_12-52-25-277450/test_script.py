def lateralsurface_cube(side_length):
    lateral_surface_area = 4 * side_length * side_length  # Calculate lateral surface area of the cube
    return lateral_surface_area

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid side length",
      "Input Data": "l=5",
      "Expected Output": "100"
    },
    {
      "Test Title": "Zero side length",
      "Input Data": "l=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Negative side length",
      "Input Data": "l=-5",
      "Expected Output": "Invalid input"
    },
    {
      "Test Title": "Invalid input",
      "Input Data": "l='abc'",
      "Expected Output": "Invalid input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()