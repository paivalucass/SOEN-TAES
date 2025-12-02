from typing import List

def select_words(s: str, n: int) -> List[str]:
    words = s.split()
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = []
    
    for word in words:
        count = sum(1 for letter in word if letter in consonants)
        if count == n:
            result.append(word)
            
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty String Input",
      "Input Data": "parameter1='', parameter2=0",
      "Expected Output": "[]"
    },
    {
      "Test Title": "String with Special Characters Input",
      "Input Data": "parameter1='Hello @#$%', parameter2=0",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Valid Input",
      "Input Data": "parameter1='Mary had a little lamb', parameter2=4",
      "Expected Output": "[\"little\"]"
    },
    {
      "Test Title": "Valid Input",
      "Input Data": "parameter1='Hello world', parameter2=4",
      "Expected Output": "[\"world\"]"
    },
    {
      "Test Title": "Valid Input",
      "Input Data": "parameter1='Uncle sam', parameter2=3",
      "Expected Output": "[\"Uncle\"]"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_select_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("simple white space", 2), [])
        self.assertEqual(select_words("Hello world", 4), ["world"])
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()