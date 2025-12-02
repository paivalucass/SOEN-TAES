from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers]
    for i in range(len(numbers) - 1, 0, -1):
        result.insert(i, delimiter)
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input List",
      "Input Data": "parameter1=[], parameter2=4",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Multiple Consecutive Delimiters",
      "Input Data": "parameter1=[1, 2, 3], parameter2=0",
      "Expected Output": "[1, 0, 2, 0, 3]"
    },
    {
      "Test Title": "Single Element Input List",
      "Input Data": "parameter1=[5], parameter2=2",
      "Expected Output": "[5]"
    },
    {
      "Test Title": "Negative Numbers",
      "Input Data": "parameter1=[-1, -2, -3], parameter2=-4",
      "Expected Output": "[-1, -4, -2, -4, -3]"
    },
    {
      "Test Title": "Empty Input for parameter2",
      "Input Data": "parameter1=[1, 2, 3], parameter2=",
      "Expected Output": "[1, 2, 3]"
    },
    {
      "Test Title": "Large input lists",
      "Input Data": "parameter1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], parameter2=0",
      "Expected Output": "[1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]"
    },
    {
      "Test Title": "Different data types for input parameters",
      "Input Data": "parameter1=['a', 'b', 'c'], parameter2='d'",
      "Expected Output": "['a', 'd', 'b', 'd', 'c']"
    },
    {
      "Test Title": "Boundary cases for parameter2",
      "Input Data": "parameter1=[1, 2, 3], parameter2=1000000000",
      "Expected Output": "[1, 1000000000, 2, 1000000000, 3]"
    },
    {
      "Test Title": "Error handling for negative test cases",
      "Input Data": "parameter1=['a', 'b', 'c'], parameter2='d'",
      "Expected Output": "Error: Invalid input data type"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])
    
    def test_intersperse(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()