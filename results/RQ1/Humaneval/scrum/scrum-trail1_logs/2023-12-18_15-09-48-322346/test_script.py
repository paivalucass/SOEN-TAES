def is_palindrome(text: str):
    # Remove special characters and spaces from the input text
    text = ''.join(e for e in text if e.isalnum())

    # Convert the input text to lowercase for case insensitivity
    text = text.lower()

    # Check if the text is a palindrome
    return text == text[::-1]
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_palindrome(''), True)
        
    def test_palindrome(self):
        self.assertEqual(is_palindrome('aba'), True)
        self.assertEqual(is_palindrome('aaaaa'), True)
        
    def test_non_palindrome(self):
        self.assertEqual(is_palindrome('zbcd'), False)

if __name__ == '__main__':
    unittest.main()