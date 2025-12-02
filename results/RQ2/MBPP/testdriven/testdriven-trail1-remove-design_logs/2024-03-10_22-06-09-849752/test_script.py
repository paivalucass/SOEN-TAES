def check_char(input_string):
    if input_string is None or not isinstance(input_string, str):
        return "Error handling"
    elif len(input_string) == 0 or input_string[0] != input_string[-1]:
        return "Invalid"
    else:
        return "Valid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()