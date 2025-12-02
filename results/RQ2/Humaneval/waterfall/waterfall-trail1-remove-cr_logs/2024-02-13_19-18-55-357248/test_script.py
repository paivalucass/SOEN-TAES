def is_palindrome(text: str):
    text = text.lower()
    text = ''.join(e for e in text if e.isalnum())  # Remove non-alphanumeric characters
    return text == text[::-1] if text else True  # Check if the string is equal to its reverse, return True for empty string

# Additional testing
print(is_palindrome('level'))  # True
print(is_palindrome('hello'))  # False
print(is_palindrome('A man a plan a canal Panama'))  # True
print(is_palindrome('racecar'))  # True
print(is_palindrome('madam'))  # True
print(is_palindrome('Was it a car or a cat I saw'))  # True
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty String Test",
      "Input Data": "text=''",
      "Expected Output": "True"
    },
    {
      "Test Title": "Palindrome String Test",
      "Input Data": "text='aba'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Non-Palindrome String Test",
      "Input Data": "text='zbcd'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Special Characters Test",
      "Input Data": "text='@#$%^&'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Mixed Case Input Test",
      "Input Data": "text='AbA'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Null Input Test",
      "Input Data": "text=None",
      "Expected Output": "False"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_palindrome(''), True)

    def test_palindrome_string(self):
        self.assertEqual(is_palindrome('aba'), True)

    def test_long_palindrome_string(self):
        self.assertEqual(is_palindrome('aaaaa'), True)

    def test_non_palindrome_string(self):
        self.assertEqual(is_palindrome('zbcd'), False)

if __name__ == '__main__':
    unittest.main()