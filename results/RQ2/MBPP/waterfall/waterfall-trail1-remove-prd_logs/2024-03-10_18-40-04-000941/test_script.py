def drop_empty(dict1):
    if not isinstance(dict1, dict):
        raise TypeError("Input must be a dictionary")
    
    return {key: value for key, value in dict1.items() if value}

# Test Cases:
{
  "requirement analysis": "The function drop_empty should take a dictionary as input and return a new dictionary with only the non-empty items.",
  "test_cases": [
    {
      "Test Title": "Empty String Test",
      "Input Data": "{'c1': '', 'c2': 'Green', 'c3': 'Blue'}",
      "Expected Output": "{'c2': 'Green', 'c3': 'Blue'}"
    },
    {
      "Test Title": "Empty List Test",
      "Input Data": "{'c1': [''], 'c2': [1, 2, 3], 'c3': ['a', 'b', 'c']}",
      "Expected Output": "{'c2': [1, 2, 3], 'c3': ['a', 'b', 'c']}"
    },
    {
      "Test Title": "None Value Test",
      "Input Data": "{'c1': None, 'c2': 'Green', 'c3': None}",
      "Expected Output": "{'c2': 'Green'}"
    },
    {
      "Test Title": "Nested Dictionaries Test",
      "Input Data": "{'c1': {'a': 1, 'b': 2}, 'c2': {'x': 'apple', 'y': 'banana'}, 'c3': {'m': [1, 2, 3], 'n': ['x', 'y', 'z']}}",
      "Expected Output": "{'c1': {'a': 1, 'b': 2}, 'c2': {'x': 'apple', 'y': 'banana'}, 'c3': {'m': [1, 2, 3], 'n': ['x', 'y', 'z']}}"
    },
    {
      "Test Title": "Multiple Data Types Test",
      "Input Data": "{'c1': 123, 'c2': [1, 2, 3], 'c3': 'xyz'}",
      "Expected Output": "{'c1': 123, 'c2': [1, 2, 3], 'c3': 'xyz'}"
    },
    {
      "Test Title": "Negative Test Case",
      "Input Data": "{'c1': '', 'c2': 'Green', 'c3': 'Blue'}",
      "Expected Output": "Error: Invalid Input"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()