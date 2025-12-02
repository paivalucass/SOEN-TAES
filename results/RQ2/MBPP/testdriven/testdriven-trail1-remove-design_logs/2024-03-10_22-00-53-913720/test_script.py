def odd_values_string(input_string):
    if isinstance(input_string, str):
        return input_string[::2]
    else:
        return "Invalid input format"
import unittest

class Test(unittest.TestCase):
    def test_odd_values_string(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()