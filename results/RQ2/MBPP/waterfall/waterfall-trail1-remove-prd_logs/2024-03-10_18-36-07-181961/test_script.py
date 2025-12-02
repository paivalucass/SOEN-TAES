def check_char(string):
    if not isinstance(string, str) or len(string) < 1:
        return "Invalid"
    
    string = string.strip()
    
    if string[0].lower() == string[-1].lower():
        return "Valid"
    else:
        return "Invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()