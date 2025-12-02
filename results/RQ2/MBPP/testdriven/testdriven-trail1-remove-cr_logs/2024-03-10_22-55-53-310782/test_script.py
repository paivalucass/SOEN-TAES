def find_adverbs(text):
    '''Write a function to find the first adverb ending with ly and its positions in a given string.'''
    words = text.split()
    for i in range(len(words)):
        if words[i].endswith('ly'):
            return '{}-{}: {}'.format(text.find(words[i]), text.find(words[i]), words[i])
import unittest

class Test(unittest.TestCase):
   def test_find_adverbs(self):
       self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-1: Clearly')

if __name__ == '__main__':
   unittest.main()