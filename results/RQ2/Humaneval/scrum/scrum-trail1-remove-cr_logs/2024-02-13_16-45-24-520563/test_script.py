from typing import List

def string_xor(a: str, b: str) -> str:
    if not all(char in '01' for char in a) or not all(char in '01' for char in b):
        return "Error"
    result = ''
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input strings with different lengths",
      "Input Data": "a='1010', b='110'",
      "Expected Output": "0100"
    },
    {
      "Test Title": "Invalid input strings with characters other than 1s and 0s",
      "Input Data": "a='01a0', b='110'",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Empty input strings",
      "Input Data": "a='', b='110'",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Invalid input strings with characters other than 1s and 0s",
      "Input Data": "a='010', b='110a'",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Invalid input strings with characters other than 1s and 0s",
      "Input Data": "a='010', b=''",
      "Expected Output": "Error"
    },
    {
      "Test Title": "Invalid input strings with characters other than 1s and 0s",
      "Input Data": "a='', b=''",
      "Expected Output": "Error"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')

if __name__ == '__main__':
    unittest.main()