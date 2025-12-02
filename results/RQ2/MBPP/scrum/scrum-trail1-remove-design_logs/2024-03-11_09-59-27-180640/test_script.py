def word_len(s):
    '''Write a python function to check whether the length of the word is odd or not.'''
    if len(s) % 2 != 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()