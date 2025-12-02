def is_lower(string):
    if isinstance(string, str):
        if string:
            return string.lower()
        else:
            return "input string is empty"
    else:
        return "input is not a valid string"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()