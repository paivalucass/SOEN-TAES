def find_literals(text, pattern):
    '''Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.'''
    try:
        match = re.search(pattern, text)
        if match:
            return (match.group(), match.start(), match.end())
        else:
            return "Pattern not found"
    except:
        return "Pattern not found"
import re
import unittest

class Test(unittest.TestCase):
    def test_find_literals(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

if __name__ == '__main__':
    unittest.main()