def odd_values_string(input_string):
    if not isinstance(input_string, str):
        return "Invalid input"
    elif len(input_string) == 0:
        return ""
    elif len(input_string) % 2 != 0:
        return "Error: Input string has odd number of characters"
    else:
        return input_string[::2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()