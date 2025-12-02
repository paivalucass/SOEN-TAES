def odd_values_string(input_string):
    if input_string is None:
        return "Error: Input is null"
    elif not isinstance(input_string, str):
        return "Error: Input is not a string"
    elif len(input_string) > 10000:
        return "Time limit exceeded"
    else:
        return input_string[::2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()