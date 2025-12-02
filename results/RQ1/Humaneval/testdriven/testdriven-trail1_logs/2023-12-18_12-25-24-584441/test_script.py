def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """

    if not text:
        return True

    # Remove non-alphanumeric characters and convert to lowercase
    formatted_text = ''.join(filter(str.isalnum, text)).lower()

    # Check if the formatted_text is a palindrome
    left = 0
    right = len(formatted_text) - 1
    while left < right:
        if formatted_text[left] != formatted_text[right]:
            return False
        left += 1
        right -= 1

    return True
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_palindrome(''), True)

    def test_palindrome_string(self):
        self.assertEqual(is_palindrome('aba'), True)
        self.assertEqual(is_palindrome('aaaaa'), True)

    def test_non_palindrome_string(self):
        self.assertEqual(is_palindrome('zbcd'), False)

if __name__ == '__main__':
    unittest.main()