def is_empty_dict(d):
    return not d

def empty_dit(list1):
    for d in list1:
        if not is_empty_dict(d):
            return False
    return True

# Testing the function with different types of input
assert empty_dit([{}, {}, {}]) == True
assert empty_dit([{}, {"a": 1}, {}]) == False
assert empty_dit([{1, 2, 3}, {}, {}]) == False
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Dictionary List",
      "Input Data": "list1=[{}, {}, {}]",
      "Expected Output": "True"
    },
    {
      "Test Title": "Non-empty Dictionary List",
      "Input Data": "list1=[{'a': 1}, {'b': '2'}, {'c': True}]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Mixed Type Values in Dictionary List",
      "Input Data": "list1=[{'a': 1, 'b': '2'}, {'c': True}, {'d': [1, 2, 3]}]",
      "Expected Output": "False"
    },
    {
      "Test Title": "Nested Dictionary List",
      "Input Data": "list1=[{'a': {'b': 1}}, {'c': {'d': '2'}}, {'e': {'f': True}}]",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_dit([{}, {}, {}]), True)

if __name__ == '__main__':
    unittest.main()