def is_upper(string):
    '''Write a python function to convert a given string to uppercase.'''
    try:
        if not isinstance(string, str):
            raise TypeError("Input is not a string")
        return string.upper()
    except TypeError as e:
        print(e)

# Test case
assert is_upper("person") == "PERSON"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_upper('person'), 'PERSON')

if __name__ == '__main__':
    unittest.main()