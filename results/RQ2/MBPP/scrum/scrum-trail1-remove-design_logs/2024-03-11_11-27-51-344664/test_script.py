def check_str(string):
    '''Function to check whether the given string is starting with a vowel or not using regex.'''
    pattern = r'^[aeiouAEIOU].*'
    if re.match(pattern, string):
        return True
    else:
        return False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(check_str('annie'))
        self.assertFalse(check_str('hello'))

if __name__ == '__main__':
    unittest.main()