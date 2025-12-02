def check_char(string):
    if len(string) == 0:
        raise ValueError("Input string cannot be empty")
    elif len(string) == 1:
        return 'Valid'
    else:
        if string[0] == string[-1]:
            return 'Valid'
        else:
            return 'Invalid'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()