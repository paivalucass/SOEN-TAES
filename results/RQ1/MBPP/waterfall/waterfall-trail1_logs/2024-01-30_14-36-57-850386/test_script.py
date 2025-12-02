def is_lower(string):
    if not isinstance(string, str):
        return "Invalid input"
    
    lower_string = string.lower()
    return lower_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()