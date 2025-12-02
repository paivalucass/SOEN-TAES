def first_repeated_char(str1):
    ''' 
    This function takes a string as input and returns the first repeated character in the given string.

    Args:
    str1: Input string

    Returns:
    The first repeated character in the given string, or None if no repeated character is found.

    Algorithm:
    - Iterate through each character in the input string
    - Maintain a set to keep track of characters seen so far
    - If a character is already in the set, return it as the first repeated character
    - If no repeated character is found, return None
    '''
    char_set = set()
    for char in str1:
        if char in char_set:
            return char
        else:
            char_set.add(char)
    return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_repeated_char('abcabc'), 'a')

if __name__ == '__main__':
    unittest.main()