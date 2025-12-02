def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if string == "":
        return ""
    else:
        for i in range(len(string)):
            if string[i:] == string[i:][::-1]:
                return string + string[:i][::-1]
import unittest

class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertFalse(is_palindrome('hello'))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome(''), '')
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')

if __name__ == '__main__':
    unittest.main()