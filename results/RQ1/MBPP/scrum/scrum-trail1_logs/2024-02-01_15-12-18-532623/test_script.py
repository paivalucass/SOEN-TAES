def sequential_search(dlist, item):
    if len(dlist) == 0 or not isinstance(item, (int, float, str)):
        return False, -1

    for index, element in enumerate(dlist):
        if element == item:
            return True, index

    return False, -1

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Array Test",
      "Input Data": "dlist=[], item=5",
      "Expected Output": "(False, -1)"
    },
    {
      "Test Title": "Multiple Occurrences Test",
      "Input Data": "dlist=[1, 2, 3, 3, 4], item=3",
      "Expected Output": "(True, 2)"
    },
    {
      "Test Title": "Element Not Found Test",
      "Input Data": "dlist=[5, 6, 7, 8], item=10",
      "Expected Output": "(False, -1)"
    },
    {
      "Test Title": "Empty List Test",
      "Input Data": "dlist=[], item=31",
      "Expected Output": "(False, -1)"
    },
    {
      "Test Title": "Very Large List Test",
      "Input Data": "dlist=[11,23,58,31,56,77,43,12,65,19]*100000, item=31",
      "Expected Output": "(True, 3)"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 31), (True, 3))

if __name__ == '__main__':
    unittest.main()