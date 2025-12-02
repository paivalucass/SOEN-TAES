def filter_data(students, min_height, min_weight):
    if not isinstance(students, dict) or not all(isinstance(height_weight, tuple) and len(height_weight) == 2 and isinstance(height_weight[0], (int, float)) and isinstance(height_weight[1], (int, float)) for height_weight in students.values()) or not isinstance(min_height, (int, float)) or not isinstance(min_weight, (int, float)):
        return "Invalid input"

    filtered_students = {name: (height, weight) for name, (height, weight) in students.items() if height >= min_height and weight >= min_weight}
    return filtered_students

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Dictionary Input",
      "Input Data": "students={}, h=5.0, w=50.0",
      "Expected Output": "{}"
    },
    {
      "Test Title": "No Students Above Minimum Height and Weight",
      "Input Data": "students={'Cierra Vega': (5.5, 60), 'Alden Cantrell': (5.7, 65)}, h=6.0, w=70.0",
      "Expected Output": "{}"
    },
    {
      "Test Title": "All Students Meet Criteria",
      "Input Data": "students={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (6.1, 65)}, h=6.0, w=60.0",
      "Expected Output": "{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (6.1, 65)}"
    },
    {
      "Test Title": "Negative Heights and Weights",
      "Input Data": "students={'Cierra Vega': (-6.2, 70), 'Alden Cantrell': (6.1, -65)}, h=6.0, w=60.0",
      "Expected Output": "{}"
    },
    {
      "Test Title": "Boundary Test for Zero Height and Weight",
      "Input Data": "students={'Cierra Vega': (0.0, 0.0), 'Alden Cantrell': (0.1, 0.1)}, h=0.0, w=0.0",
      "Expected Output": "{}"
    },
    {
      "Test Title": "Boundary Test for Large Height and Weight",
      "Input Data": "students={'Cierra Vega': (100.0, 100.0), 'Alden Cantrell': (200.0, 200.0)}, h=1000.0, w=1000.0",
      "Expected Output": "{}"
    },
    {
      "Test Title": "Specific Error Message for Negative Heights and Weights",
      "Input Data": "students={'Cierra Vega': (-6.2, 70), 'Alden Cantrell': (6.1, -65)}, h=6.0, w=60.0",
      "Expected Output": "Error: Negative heights and weights provided"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}, 6.0, 70), {'Cierra Vega': (6.2, 70)})

if __name__ == '__main__':
    unittest.main()