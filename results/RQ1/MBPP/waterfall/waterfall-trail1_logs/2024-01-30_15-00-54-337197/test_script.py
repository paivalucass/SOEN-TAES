import re

def check_str(string):
    # Write a function to check whether the given string is starting with a vowel or not using regex.
    pattern = r'^(?i)[aeiou]'
    return bool(re.match(pattern, string))
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))

if __name__ == '__main__':
    unittest.main()