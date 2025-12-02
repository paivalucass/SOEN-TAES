def check_char(string):
    if string is None:
        return "Null input"
    if len(string) == 0:
        return "Empty string"
    
    string = string.strip().lower()
    
    if string[0] == string[-1]:
        return "Valid"
    else:
        return "Invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()