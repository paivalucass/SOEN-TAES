import unittest

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    """
    if len(text) <= 1:
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False

class TestPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_palindrome(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

if __name__ == '__main__':
    unittest.main()
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