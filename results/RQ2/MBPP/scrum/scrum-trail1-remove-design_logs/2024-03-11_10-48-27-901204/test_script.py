def extract_values(text):
    import re
    values = re.findall(r'\"(.*?)\"', text)
    return values
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Extract values from simple string",
      "Input Data": "text='\"Python\", \"PHP\", \"Java\"'",
      "Expected Output": "['Python', 'PHP', 'Java']"
    },
    {
      "Test Title": "Extract values from empty string",
      "Input Data": "text=''",
      "Expected Output": "[]"
    },
    {
      "Test Title": "Extract values from string with special characters",
      "Input Data": "text='\"@Python@\", \"#PHP#\", \"&Java&\"'",
      "Expected Output": "['@Python@', '#PHP#', '&Java&']"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_values('"Python", "PHP", "Java"'), ['Python', 'PHP', 'Java'])

if __name__ == '__main__':
    unittest.main()