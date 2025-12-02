def is_lower(string):
    if not isinstance(string, str):
        return "Invalid input: input is not a string"
    if string == "":
        return ""
    return string.lower()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()