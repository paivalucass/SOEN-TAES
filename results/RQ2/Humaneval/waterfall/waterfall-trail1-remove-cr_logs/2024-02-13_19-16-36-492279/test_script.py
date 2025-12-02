def unique(l: list) -> list:
    try:
        if not l:
            return []  
        for element in l:
            if not isinstance(element, int):
                raise ValueError("Input list contains non-integer elements")  
        unique_list = list(set(l))  
        unique_list.sort()  
        return unique_list
    except ValueError as e:
        return str(e)  

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input List Test",
      "Input Data": "[]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Non-Integer Elements Test",
      "Input Data": "['a', 1, 2, 3]",
      "Expected Output": "Input list contains non-integer elements"
    },
    {
      "Test Title": "Sorted Unique Elements Test",
      "Input Data": "[5, 3, 5, 2, 3, 3, 9, 0, 123]",
      "Expected Output": "[0, 2, 3, 5, 9, 123]"
    },
    {
      "Test Title": "Single Element Test",
      "Input Data": "[1]",
      "Expected Output": "[1]"
    },
    {
      "Test Title": "Empty Input List Boundary Value Test",
      "Input Data": "[]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Large Input List Boundary Value Test",
      "Input Data": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]",
      "Expected Output": "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]"
    },
    {
      "Test Title": "Negative Numbers Test",
      "Input Data": "[-1, -2, -3, -4, -5]",
      "Expected Output": "[-5, -4, -3, -2, -1]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == '__main__':
    unittest.main()