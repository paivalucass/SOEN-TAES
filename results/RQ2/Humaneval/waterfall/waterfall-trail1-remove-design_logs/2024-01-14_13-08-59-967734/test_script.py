def is_palindrome(text: str):
    text = text.strip().lower()
    return text == text[::-1]
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