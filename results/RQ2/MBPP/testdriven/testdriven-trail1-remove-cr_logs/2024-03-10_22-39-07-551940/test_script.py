def check_char(string):
    if string == "":
        return "Invalid"
    
    import re
    if re.match(r'^(.).*\1$', string):
        return "Valid"
    else:
        return "Invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()