def odd_values_string(input_string):
    if not isinstance(input_string, str) or len(input_string) == 0:
        return "Error: Input parameter is not a valid string."

    return input_string[::2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()