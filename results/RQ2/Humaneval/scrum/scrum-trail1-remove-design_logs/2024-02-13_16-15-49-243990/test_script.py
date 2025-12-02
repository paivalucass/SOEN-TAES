def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    count = sum(1 for i in range(0, len(s), 2) if s[i] in ['A', 'E', 'I', 'O', 'U'])
    return count

# Test Cases:
{
  "revised_test_cases": [
    {
      "Test Title": "Uppercase Vowels at Even Indices - Empty Input",
      "Input Data": "s=''",
      "Expected Output": "0"
    },
    {
      "Test Title": "Uppercase Vowels at Even Indices - Special Characters",
      "Input Data": "s='@BCdE#'",
      "Expected Output": "1"
    },
    {
      "Test Title": "Uppercase Vowels at Even Indices - Long String",
      "Input Data": "s='aBCdEfghijklmnopqrstuvwxyzABCDEfghijklmnopqrstuvwxyz'",
      "Expected Output": "4"
    },
    {
      "Test Title": "No Uppercase Vowels at Even Indices - Boundary Case",
      "Input Data": "s='a'",
      "Expected Output": "0"
    },
    {
      "Test Title": "No Uppercase Vowels at Even Indices - Negative Case",
      "Input Data": "s='A'",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()