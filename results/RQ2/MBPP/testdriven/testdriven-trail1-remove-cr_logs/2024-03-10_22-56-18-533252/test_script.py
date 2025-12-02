def text_match_three(text: str) -> bool:
    '''Write a function that matches a string that has an 'a' followed by three 'b's.
    Input: text (string) - The input string to be checked
    Output: bool - True if the input string has an 'a' followed by three 'b's, False otherwise
    '''
    if 'a' in text and 'b' in text and text.count('b') >= 3 and text.index('a') < text.index('b'):
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(text_match_three('abbb'), True)
        self.assertEqual(text_match_three('ac'), False)

if __name__ == '__main__':
    unittest.main()