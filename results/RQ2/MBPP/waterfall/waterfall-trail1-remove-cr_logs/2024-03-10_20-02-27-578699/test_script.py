def check_char(string):
    if len(string) < 1:
        return "Invalid"
    else:
        return "Valid" if string[0] == string[-1] else "Invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()