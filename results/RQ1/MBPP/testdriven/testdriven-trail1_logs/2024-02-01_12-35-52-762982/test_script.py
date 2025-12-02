def check_char(string): 
    if (not isinstance(string, str)) or (string is None) or (string == ''):
        return "Invalid"
    
    if len(string) == 1:
        return "Valid"
    
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