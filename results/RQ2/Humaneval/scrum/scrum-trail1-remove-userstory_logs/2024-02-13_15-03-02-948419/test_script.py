def get_positive(input_list: list) -> list:
    return [x for x in input_list if x > 0]

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty list input",
      "Input Data": "[]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "List with positive and negative numbers",
      "Input Data": "[-1, 2, -4, 5, 6]",
      "Expected Output": "[2, 5, 6]"
    },
    {
      "Test Title": "List with all negative numbers",
      "Input Data": "[-1, -2, -3, -4]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "List with all positive numbers",
      "Input Data": "[1, 2, 3, 4]",
      "Expected Output": "[1, 2, 3, 4]"
    },
    {
      "Test Title": "Mix of positive and negative numbers and zero",
      "Input Data": "[-1, 0, 2, -4, 5, 6]",
      "Expected Output": "[2, 5, 6]"
    },
    {
      "Test Title": "Large number of elements",
      "Input Data": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]",
      "Expected Output": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()