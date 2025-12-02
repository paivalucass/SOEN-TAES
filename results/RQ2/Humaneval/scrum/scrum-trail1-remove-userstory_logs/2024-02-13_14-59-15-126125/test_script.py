def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - If the string is already a palindrome, return it.
    - Otherwise, append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return string + string[:-1][::-1]
import unittest

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('abcba'))
        self.assertTrue(is_palindrome('radar'))
        self.assertFalse(is_palindrome('hello'))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(''), '')
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')

if __name__ == '__main__':
    unittest.main()