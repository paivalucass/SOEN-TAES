def number_of_substrings(input_str):
    count = (len(input_str) * (len(input_str) + 1)) // 2
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test case for empty string input",
      "Input Data": "parameter1=''",
      "Expected Output": "0"
    },
    {
      "Test Title": "Test case for strings with different lengths",
      "Input Data": "parameter1='a', parameter2='abc'",
      "Expected Output": "1, 6"
    },
    {
      "Test Title": "Test case for strings with special characters",
      "Input Data": "parameter1='a@b', parameter2='1#2#3'",
      "Expected Output": "3, 6"
    },
    {
      "Test Title": "Test case for error handling scenarios",
      "Input Data": "parameter1=123, parameter2='abc'",
      "Expected Output": "0, 6"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_number_of_substrings(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()