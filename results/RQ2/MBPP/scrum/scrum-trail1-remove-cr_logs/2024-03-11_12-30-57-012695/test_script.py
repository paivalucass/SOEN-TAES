def remove_Occ(s, ch):
    first_occurrence = s.find(ch)
    last_occurrence = s.rfind(ch)
    
    if first_occurrence == -1 or last_occurrence == -1:
        return "Character not found in the string"
    
    s = s[:first_occurrence] + s[first_occurrence+1:last_occurrence] + s[last_occurrence+1:]
    
    return s
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test function with different edge cases",
      "Input Data": "parameter1=\"\", parameter2=\"h\"",
      "Expected Output": "e"
    },
    {
      "Test Title": "Test for accuracy and reliability",
      "Input Data": "parameter1=\"hello world\", parameter2=\"o\"",
      "Expected Output": "hell wrld"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_Occ("hello", "l"), "heo")

if __name__ == '__main__':
    unittest.main()