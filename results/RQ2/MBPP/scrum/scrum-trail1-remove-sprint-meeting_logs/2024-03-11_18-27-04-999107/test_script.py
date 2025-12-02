def odd_values_string(input_string):
    if not isinstance(input_string, str) or not input_string:
        return "Invalid input: input_string must be a non-empty string."
    
    return input_string[::2]  # Return the string with characters at even index values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()