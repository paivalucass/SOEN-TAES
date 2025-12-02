def add(lst):
    if not lst:
        return "Error: Empty list"
    
    if len(lst) < 2:
        return "Error: List should have at least 2 elements"
    
    result = 0
    for i in range(1, len(lst), 2):
        if isinstance(lst[i], int) and lst[i] % 2 == 0:
            result += lst[i]
    
    if result == 0:
        return "Error: No even elements at odd indices"
    else:
        return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty List",
      "Input Data": "parameter1=[]",
      "Expected Output": "Error: Empty list"
    },
    {
      "Test Title": "List with only odd numbers",
      "Input Data": "parameter1=[1, 3, 5, 7]",
      "Expected Output": "Error: No even elements at odd indices"
    },
    {
      "Test Title": "List with both even and odd numbers at odd indices",
      "Input Data": "parameter1=[2, 3, 4, 5, 6]",
      "Expected Output": "10"
    },
    {
      "Test Title": "List with only one element",
      "Input Data": "parameter1=[4]",
      "Expected Output": "Error: List should have at least 2 elements"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()