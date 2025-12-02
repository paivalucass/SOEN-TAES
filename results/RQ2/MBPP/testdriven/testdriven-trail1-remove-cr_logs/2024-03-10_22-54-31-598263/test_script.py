import re

def text_starta_endb(text):
    '''
    Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
    The function should use regular expressions to match the specified pattern.

    Input:
    - text: string

    Output:
    - True if the input string matches the pattern
    - False if the input string does not match the pattern

    Error Handling:
    - Handle any exceptions related to regular expression matching

    Performance and Scalability Considerations:
    - Optimize the regular expression pattern for efficiency and scalability
    '''
    try:
        if re.match('^a.*b$', text):
            return True
        else:
            return False
    except re.error:
        return False

# Example usage
assert text_starta_endb("aabbbb")
import unittest

class Test(unittest.TestCase):
    def test_starta_endb(self):
        self.assertTrue(text_starta_endb('aabbbb'))

if __name__ == '__main__':
    unittest.main()