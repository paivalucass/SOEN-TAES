def find_literals(text, pattern):
    '''Write a function to search a string for a regex pattern. The function should return the matching substring, start index and end index.
    If the pattern is not found in the text, the function should return None.'''
    
    import re
    
    match = re.search(pattern, text)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'), ('fox', 16, 19))

if __name__ == '__main__':
    unittest.main()