def is_lower(string):
    if not isinstance(string, str):
        raise ValueError("Error: Non-string input")
    elif string == "":
        raise ValueError("Error: Empty string input")
     
    return string.lower()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()