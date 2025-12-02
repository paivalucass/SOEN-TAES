def overlapping(list1, list2):
    try:
        if any(item in list2 for item in list1):
            return True
        else:
            return False
    except (ValueError, TypeError):
        print("Invalid inputs provided")
        return None

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Check for overlapping values in two sequences with duplicate values",
      "Input Data": "list1=[1,1,2,3,4,5,5],list2=[5,6,6,7,8,9,9]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Check for overlapping values in two sequences with large number of values",
      "Input Data": "list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],list2=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Check for overlapping values in two sequences with special characters",
      "Input Data": "list1=['!','@','#','$','%','^'],list2=['&','*','(',')','-','+']",
      "Expected Output": "False"
    },
    {
      "Test Title": "Check for overlapping values in two sequences with strings and floats",
      "Input Data": "list1=[1.5,2.5,3.5,4.5,5.5],list2=[5.5,6.5,7.5,8.5,9.5]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Check for overlapping values in two empty sequences",
      "Input Data": "list1=[],list2=[]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Check for overlapping values in two sequences with one common value",
      "Input Data": "list1=[1,2,3,4,5],list2=[5,6,7,8,9]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Check for overlapping values in two sequences for performance testing",
      "Input Data": "list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],list2=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]",
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