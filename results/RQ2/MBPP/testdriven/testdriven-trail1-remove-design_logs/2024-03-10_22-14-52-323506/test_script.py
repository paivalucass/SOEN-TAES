def is_upper(string):
    if isinstance(string, str):
        return string.upper()
    else:
        return "Error: Invalid Input Type"
import unittest

class Test(unittest.TestCase):
    def test_uppercase_conversion(self):
        self.assertEqual(is_upper('person'), 'PERSON')

if __name__ == '__main__':
    unittest.main()