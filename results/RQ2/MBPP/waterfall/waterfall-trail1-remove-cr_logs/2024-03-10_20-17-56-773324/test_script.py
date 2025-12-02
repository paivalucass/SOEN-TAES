def check_expression(exp):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in exp:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Expression",
      "Input Data": "exp=''",
      "Expected Output": "false"
    },
    {
      "Test Title": "Balanced Expression",
      "Input Data": "exp='{()}[{}]'",
      "Expected Output": "true"
    },
    {
      "Test Title": "Unbalanced Expression",
      "Input Data": "exp='{(})[{}]'",
      "Expected Output": "false"
    },
    {
      "Test Title": "Long Expression",
      "Input Data": "exp='{{{{{}}}}}'",
      "Expected Output": "true"
    },
    {
      "Test Title": "Special Characters",
      "Input Data": "exp='{{@#$%}}'",
      "Expected Output": "true"
    },
    {
      "Test Title": "Nested Brackets",
      "Input Data": "exp='{{(())}}'",
      "Expected Output": "true"
    },
    {
      "Test Title": "One Type of Bracket",
      "Input Data": "exp='{{{{{{'",
      "Expected Output": "false"
    },
    {
      "Test Title": "Empty Input Data",
      "Input Data": "exp=''",
      "Expected Output": "true"
    },
    {
      "Test Title": "Null Input Data",
      "Input Data": "exp=null",
      "Expected Output": "false"
    },
    {
      "Test Title": "Input Data with Trailing Spaces",
      "Input Data": "exp='{{}}   '",
      "Expected Output": "true"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_check_expression(self):
        self.assertTrue(check_expression("{()}[{}]"))

if __name__ == '__main__':
    unittest.main()