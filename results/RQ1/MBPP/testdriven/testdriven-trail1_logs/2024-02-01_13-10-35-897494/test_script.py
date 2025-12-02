def is_upper(string):
    '''Write a python function to convert a given string to uppercase.'''
    if isinstance(string, str):
        if string:
            return string.upper()
        else:
            return "Error: Input string is empty"
    else:
        return "Error: Input is not a string"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_upper('person'), 'PERSON')

if __name__ == '__main__':
    unittest.main()