def is_lower(string):
    """
    Write a python function to convert the given string to lower case.
    """
    if isinstance(string, str):
        return string.lower()
    else:
        raise ValueError("Input is not a string")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()