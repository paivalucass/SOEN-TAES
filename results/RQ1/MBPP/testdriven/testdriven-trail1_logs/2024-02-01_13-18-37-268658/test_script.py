def check_str(string):
    '''Write a function to check whether the given string is starting with a vowel or not using if condition.'''
    if string[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

assert check_str("annie")
import unittest
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_str('annie'), True)

if __name__ == '__main__':
    unittest.main()