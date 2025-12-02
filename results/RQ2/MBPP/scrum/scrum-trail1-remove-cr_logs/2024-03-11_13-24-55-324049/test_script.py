def combinations_list(list1):
    if not all(isinstance(item, str) for item in list1):
        return "Error: Invalid element in input list"
    
    results = [[]]
    for item in list1:
        results.extend([prev + [item] for prev in results])
    
    return results

# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "Empty List Input",
      "Input Data": "list1=[]",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Valid Input List",
      "Input Data": "list1=['orange', 'red', 'green', 'blue']",
      "Expected Output": "[[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']]"
    },
    {
      "Test Title": "Invalid Element in List",
      "Input Data": "list1=['orange', 1, 'green', 'blue']",
      "Expected Output": "Error: Invalid element in input list"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_list(['orange', 'red', 'green', 'blue']), [[], ['orange'], ['red'], ['orange', 'red'], ['green'], ['orange', 'green'], ['red', 'green'], ['orange', 'red', 'green'], ['blue'], ['orange', 'blue'], ['red', 'blue'], ['orange', 'red', 'blue'], ['green', 'blue'], ['orange', 'green', 'blue'], ['red', 'green', 'blue'], ['orange', 'red', 'green', 'blue']])

if __name__ == '__main__':
    unittest.main()