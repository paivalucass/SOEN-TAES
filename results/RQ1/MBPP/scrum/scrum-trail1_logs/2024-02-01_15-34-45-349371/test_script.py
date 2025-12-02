def overlapping(list1, list2):
    return any(item in list2 for item in list1)

assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Sequences",
      "Input Data": "parameter1=[], parameter2=[1,2,3]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Different Data Types",
      "Input Data": "parameter1=[1, 'a', 3], parameter2=[3, 'b', 4]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Large Input Sequences",
      "Input Data": "parameter1=[1,2,3,4,5,6,7,8,9,10], parameter2=[11,12,13,14,15]",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(overlapping([1,2,3,4,5],[6,7,8,9]), False)

if __name__ == '__main__':
    unittest.main()