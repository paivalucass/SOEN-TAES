def extract_string(str_list, l):
    '''Write a function to extract specified size of strings from a given list of string values.'''
    result = [s for s in str_list if len(s) >= l]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()