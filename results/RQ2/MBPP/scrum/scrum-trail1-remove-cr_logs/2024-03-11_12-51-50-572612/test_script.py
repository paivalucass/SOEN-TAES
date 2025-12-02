def check_type(test_tuple):
    if len(test_tuple) == 0:
        return True
    data_type = type(test_tuple[0])
    for element in test_tuple:
        if type(element) != data_type:
            return False
    return True

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Check if all elements in tuple have the same data type with empty tuple",
      "Input Data": "test_tuple=()",
      "Expected Output": "True"
    },
    {
      "Test Title": "Check if all elements in tuple have the same data type with single element tuple",
      "Input Data": "test_tuple=(5,)",
      "Expected Output": "True"
    },
    {
      "Test Title": "Check if all elements in tuple have the same data type with string elements",
      "Input Data": "test_tuple=('hello', 'world', '123')",
      "Expected Output": "True"
    },
    {
      "Test Title": "Check if all elements in tuple have the same data type with mixed data types",
      "Input Data": "test_tuple=(1, 'hello', True)",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_type((5, 6, 7, 3, 5, 6)), True)

if __name__ == '__main__':
    unittest.main()