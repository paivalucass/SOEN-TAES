def first_repeated_char(str1):
    char_map = {}
    for char in str1:
        if char in char_map:
            return char
        char_map[char] = 1
    return None
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test with empty string",
      "Input Data": "parameter1='', parameter2=''",
      "Expected Output": ""
    },
    {
      "Test Title": "Test with no repeated characters",
      "Input Data": "parameter1='abcdef', parameter2='123'",
      "Expected Output": ""
    },
    {
      "Test Title": "Test with repeated characters",
      "Input Data": "parameter1='abcabc', parameter2='123'",
      "Expected Output": "a"
    },
    {
      "Test Title": "Test with special characters",
      "Input Data": "parameter1='a#b$c', parameter2='123'",
      "Expected Output": "#"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()