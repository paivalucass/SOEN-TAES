def is_sublist(l, s):
    if not isinstance(l, list) or not isinstance(s, list):
        raise TypeError("Both input parameters should be lists")
    
    if len(s) == 0:
        return True
    
    for i in range(len(l)):
        if l[i:i+len(s)] == s:
            return True
    
    return False

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Check if list contains the given sublist - Positive case",
      "Input Data": "l=[1,2,3,4,5], s=[2,3]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Check if list contains the given sublist - Negative case",
      "Input Data": "l=[1,2,3,4,5], s=[6,7]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Check if empty list contains the given sublist",
      "Input Data": "l=[], s=[1,2,3]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Check if sublist is longer than the main list",
      "Input Data": "l=[1,2,3], s=[4,5,6,7]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Check if sublist is the same as the main list",
      "Input Data": "l=[1,2,3], s=[1,2,3]",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_sublist([2,4,3,5,7],[3,7]), False)

if __name__ == '__main__':
    unittest.main()