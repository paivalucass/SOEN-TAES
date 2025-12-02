def remove_odd(str1):
    if type(str1) != str:
        return "Error"
    else:
        new_string = str1[1::2]
        return new_string

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test for empty input string",
      "Input Data": "parameter1=''",
      "Expected Output": ""
    },
    {
      "Test Title": "Test for input string with only odd characters",
      "Input Data": "parameter1='abcde'",
      "Expected Output": "b"
    },
    {
      "Test Title": "Test for input string with only even characters",
      "Input Data": "parameter1='abcdef'",
      "Expected Output": "bdf"
    },
    {
      "Test Title": "Test for input string with a mix of both odd and even characters",
      "Input Data": "parameter1='abcdefgh'",
      "Expected Output": "bdf"
    },
    {
      "Test Title": "Test for special characters in input string",
      "Input Data": "parameter1='ab@cde#fgh'",
      "Expected Output": "bdf"
    },
    {
      "Test Title": "Test for non-string input",
      "Input Data": "parameter1=123",
      "Expected Output": "Error"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd('python'), 'yhn')

if __name__ == '__main__':
    unittest.main()