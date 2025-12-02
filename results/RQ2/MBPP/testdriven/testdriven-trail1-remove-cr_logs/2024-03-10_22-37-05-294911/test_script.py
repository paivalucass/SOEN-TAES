def text_match_two_three(text):
    '''Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.'''
    if not text:
        raise ValueError("Input string is empty")

    for index in range(len(text) - 2):
        if text[index] == 'a' and text[index+1:index+3] in ['bb', 'bbb']:
            return True

    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()