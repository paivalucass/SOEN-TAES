def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty String Test",
      "Input Data": "string='', substring='a'",
      "Expected Output": "0"
    },
    {
      "Test Title": "Single Character String Test",
      "Input Data": "string='aaa', substring='a'",
      "Expected Output": "3"
    },
    {
      "Test Title": "Overlapping Substring Test",
      "Input Data": "string='aaaa', substring='aa'",
      "Expected Output": "3"
    },
    {
      "Test Title": "Special Character Test",
      "Input Data": "string='a@b#c$d%', substring='$d%'",
      "Expected Output": "1"
    },
    {
      "Test Title": "Invalid Character Test",
      "Input Data": "string='abcd', substring='$d%'",
      "Expected Output": "0"
    },
    {
      "Test Title": "Null Values Test",
      "Input Data": "string='', substring=null",
      "Expected Output": "0"
    },
    {
      "Test Title": "Boundary Test Case for Substring Length",
      "Input Data": "string='aaaa', substring='aaa'",
      "Expected Output": "2"
    },
    {
      "Test Title": "Large Input Strings Test",
      "Input Data": "string='a' * 1000000, substring='a' * 1000",
      "Expected Output": "991"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_character_string(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_multiple_character_string(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()