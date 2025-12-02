import re

def text_match_one(text):
    '''Write a function that matches a string that has an a followed by one or more b's.'''
    pattern = r'a+b+'
    return bool(re.search(pattern, text))

assert text_match_one("ac")==False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()