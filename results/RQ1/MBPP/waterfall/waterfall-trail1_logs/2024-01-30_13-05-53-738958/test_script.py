def check_char(string):
    if not isinstance(string, str):
        return "Invalid input: input must be a string"
    elif len(string) < 2:
        return "Invalid input: string must have at least 2 characters"
    elif string[0] == string[-1]:
        return "Valid"
    else:
        return "Invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()