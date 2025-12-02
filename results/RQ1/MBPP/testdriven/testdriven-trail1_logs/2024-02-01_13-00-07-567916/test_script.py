def find_adverbs(text):
    '''
    Write a function to find the first adverb ending with ly and its position in a given string.
    It should return the position and adverb found as a string in the format 'start-end: adverb'.
    If no adverbs are found, it should return an empty string.
    '''
    import re
    pattern = r'\b\w+ly\b'
    match = re.search(pattern, text)
    if match:
        return f'{match.start()}-{match.end()}: {match.group()}'
    else:
        return ''
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()