def is_bored(S):
    import re
    pattern = r'\bI\b'
    sentences = re.split(r'[.!?]', S)
    count = 0
    for sentence in sentences:
        if re.match(pattern, sentence.strip()):
            count += 1
    return count
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty input",
      "Input Data": "parameter1=''",
      "Expected Output": 0
    },
    {
      "Test Title": "Large input strings",
      "Input Data": "parameter1='The sky is blue. The sun is shining. I love this weather'",
      "Expected Output": 0
    },
    {
      "Test Title": "Special characters",
      "Input Data": "parameter1='I am happy! I am sad? I am bored.'",
      "Expected Output": 3
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

if __name__ == '__main__':
    unittest.main()