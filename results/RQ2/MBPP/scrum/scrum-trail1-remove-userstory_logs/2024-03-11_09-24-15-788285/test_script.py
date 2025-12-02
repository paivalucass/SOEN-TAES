def check_str(string):
    '''Function to check whether the given string is starting with a vowel or not using regex.'''
    # Check if the input string is empty
    if not string:
        raise ValueError("Input string cannot be empty")
    
    # Regex pattern to check for the starting vowel
    pattern = r'^[aeiouAEIOU].*'

    # Return True if the pattern matches the string, False otherwise
    return bool(re.match(pattern, string))
import unittest
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))

if __name__ == '__main__':
    unittest.main()