def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    Args:
    text: the string to be checked

    Returns:
    True if the string is a palindrome, False otherwise
    """

    if not isinstance(text, str):
        return False
    
    text = text.strip()  # Remove leading and trailing whitespaces
    
    if len(text) < 2:  # Empty string or string with single character is considered palindrome
        return True
    
    return text == text[::-1]  # Check if the text is equal to its reverse
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_palindrome(''), True)

    def test_single_character_palindrome(self):
        self.assertEqual(is_palindrome('a'), True)

    def test_even_length_palindrome(self):
        self.assertEqual(is_palindrome('aba'), True)

    def test_odd_length_palindrome(self):
        self.assertEqual(is_palindrome('aaaaa'), True)

    def test_non_palindrome(self):
        self.assertEqual(is_palindrome('zbcd'), False)

if __name__ == '__main__':
    unittest.main()