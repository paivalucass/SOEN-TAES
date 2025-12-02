def is_palindrome(string: str) -> bool:
    """
    Test if given string is a palindrome
    """
    # Check if the string is equal to its reverse
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """
    Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # If the string is empty, return an empty string
    if string == "":
        return ""
    
    # Iterate through the string to find the longest postfix that is a palindrome
    for i in range(len(string)):
        if string[i:] == string[i:][::-1]:
            # If a palindromic suffix is found, append the reverse of the prefix to the end of the string
            return string + string[:i][::-1]
    
    # If no palindromic suffix is found, append the reverse of all characters except the last one to the end of the string
    return string + string[:-1][::-1]
import unittest

class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('radar'))

    def test_make_palindrome(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')

if __name__ == '__main__':
    unittest.main()