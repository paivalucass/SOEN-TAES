def is_lower(input_string):
    if isinstance(input_string, str) and input_string != '':
        return input_string.lower()
    else:
        return "Error: Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()