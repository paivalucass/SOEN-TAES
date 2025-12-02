def remove_whitespaces(text1):
    return ''.join(text1.split())
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Remove whitespaces from string",
      "Input Data": "parameter1=' Google    Flutter '",
      "Expected Output": "'GoogleFlutter'"
    },
    {
      "Test Title": "Empty string input",
      "Input Data": "parameter1=''",
      "Expected Output": "''"
    },
    {
      "Test Title": "String with only whitespaces input",
      "Input Data": "parameter1='    '",
      "Expected Output": "''"
    },
    {
      "Test Title": "String with leading whitespaces input",
      "Input Data": "parameter1='   GoogleFlutter'",
      "Expected Output": "'GoogleFlutter'"
    },
    {
      "Test Title": "String with trailing whitespaces input",
      "Input Data": "parameter1='GoogleFlutter   '",
      "Expected Output": "'GoogleFlutter'"
    },
    {
      "Test Title": "String with special characters",
      "Input Data": "parameter1=' Google!@#Flutter '",
      "Expected Output": "'Google!@#Flutter'"
    },
    {
      "Test Title": "String with null input",
      "Input Data": "parameter1=null",
      "Expected Output": "null"
    },
    {
      "Test Title": "String with undefined input",
      "Input Data": "parameter1=undefined",
      "Expected Output": "undefined"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_remove_whitespaces(self):
        self.assertEqual(remove_whitespaces(' Google    Flutter '), 'GoogleFlutter')

if __name__ == '__main__':
    unittest.main()