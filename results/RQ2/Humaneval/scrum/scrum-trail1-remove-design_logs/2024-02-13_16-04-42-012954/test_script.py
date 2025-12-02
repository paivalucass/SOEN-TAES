def is_palindrome(text: str) -> bool:
    if text is None or type(text) is not str:
        return False

    if len(text) <= 1:
        return True

    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True
# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty string",
      "Input Data": "text=''",
      "Expected Output": "True"
    },
    {
      "Test Title": "Palindrome with odd length",
      "Input Data": "text='aba'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Palindrome with even length",
      "Input Data": "text='aaaaa'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Non-palindrome",
      "Input Data": "text='zbcd'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Special characters",
      "Input Data": "text='@#$%^&*'",
      "Expected Output": "False"
    },
    {
      "Test Title": "Numbers",
      "Input Data": "text='12321'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Different language characters",
      "Input Data": "text='\u4e0a\u6d77\u81ea\u4f86\u6c34\u4f86\u81ea\u6d77\u4e0a'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Large input strings",
      "Input Data": "text='a' * 1000000",
      "Expected Output": "True"
    },
    {
      "Test Title": "Negative test case - null value",
      "Input Data": "text=null",
      "Expected Output": "False"
    },
    {
      "Test Title": "Negative test case - undefined value",
      "Input Data": "text=undefined",
      "Expected Output": "False"
    },
    {
      "Test Title": "Boundary test case - minimum allowed length",
      "Input Data": "text='a'",
      "Expected Output": "True"
    },
    {
      "Test Title": "Boundary test case - maximum allowed length",
      "Input Data": "text='a' * 1000000",
      "Expected Output": "True"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrome_string(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome_string(self):
        self.assertFalse(is_palindrome('zbcd'))

if __name__ == '__main__':
    unittest.main()