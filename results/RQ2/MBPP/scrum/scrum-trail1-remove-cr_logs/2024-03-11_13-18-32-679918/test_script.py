def text_match_one(text):
    '''Write a function that matches a string that has an a followed by one or more b's.'''
    if 'ab' in text:
        return True
    else:
        return False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()