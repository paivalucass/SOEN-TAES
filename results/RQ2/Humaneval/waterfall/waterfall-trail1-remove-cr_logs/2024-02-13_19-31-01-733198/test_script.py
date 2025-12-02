def find_max(words):
    if not words:
        return "Error: Empty list input"

    max_unique_char_count = 0
    max_unique_char_word = ""

    for word in words:
        unique_chars = set(word)
        unique_char_count = len(unique_chars)

        if unique_char_count > max_unique_char_count:
            max_unique_char_count = unique_char_count
            max_unique_char_word = word
        elif unique_char_count == max_unique_char_count and word < max_unique_char_word:
            max_unique_char_word = word

    return max_unique_char_word

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Input List",
      "Input Data": "[]",
      "Expected Output": ""
    },
    {
      "Test Title": "Single Word Input List",
      "Input Data": "['hello']",
      "Expected Output": "hello"
    },
    {
      "Test Title": "Input List with Non-Alphabetic Characters",
      "Input Data": "['abc123', 'def$%^', 'ghi&*()']",
      "Expected Output": "abc123"
    },
    {
      "Test Title": "Multiple Strings with Maximum Unique Characters",
      "Input Data": "['name', 'enam', 'game']",
      "Expected Output": "enam"
    },
    {
      "Test Title": "Input List with Duplicate Words",
      "Input Data": "['hello', 'hello']",
      "Expected Output": "hello"
    },
    {
      "Test Title": "Input List with Special Characters Only",
      "Input Data": "['$%^&*()', '!@#$%^', '&*()_+']",
      "Expected Output": "$%^&*()"
    },
    {
      "Test Title": "Input List with a Mix of Uppercase and Lowercase Words",
      "Input Data": "['Hello', 'hElLo', 'HELLO']",
      "Expected Output": "Hello"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb" ,"cc"]), "aaaaaaa")

if __name__ == '__main__':
    unittest.main()