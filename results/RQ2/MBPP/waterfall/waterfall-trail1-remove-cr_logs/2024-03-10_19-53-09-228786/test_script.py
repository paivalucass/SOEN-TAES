def sort_sublists(input_list):
    sorted_list = [sorted(sublist) for sublist in input_list]
    return sorted_list

# Test Cases:
{
  "TestCases": [
    {
      "Test Title": "Sort sublists of strings in a list of lists with different lengths and types of sublists",
      "Input Data": "input_list=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]",
      "Expected Output": "[['black', 'white'], ['green', 'orange'], ['black', 'orange', 'white']]"
    },
    {
      "Test Title": "Sort sublists of strings in an empty input list",
      "Input Data": "input_list=[]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Sort sublists of strings in an input list with edge cases",
      "Input Data": "input_list=[['a', 'c', 'b'], ['z', 'x'], ['h']]",
      "Expected Output": "[['a', 'b', 'c'], ['h'], ['x', 'z']]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_sort_sublists(self):
        self.assertEqual(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()