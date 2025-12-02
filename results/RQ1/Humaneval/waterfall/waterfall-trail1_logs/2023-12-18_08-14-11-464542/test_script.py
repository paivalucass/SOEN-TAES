def is_palindrome(text: str) -> bool:
    alphanumeric_text = ''.join(e for e in text if e.isalnum())
    lowercase_text = alphanumeric_text.lower()
    return lowercase_text == lowercase_text[::-1]
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