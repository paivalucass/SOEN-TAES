def is_bored(S):
    sentences = S.split(".")
    count = 0
    for sentence in sentences:
        words = sentence.strip().split()
        if len(words) > 0 and words[0] == "I":
            count += 1
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "No sentences start with 'I'",
      "Input Data": "S='Hello world'",
      "Expected Output": "0"
    },
    {
      "Test Title": "One sentence starts with 'I'",
      "Input Data": "S='The sky is blue. The sun is shining. I love this weather'",
      "Expected Output": "1"
    },
    {
      "Test Title": "Empty input",
      "Input Data": "S=''",
      "Expected Output": "0"
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