def odd_values_string(input_string):
    if not isinstance(input_string, str) or len(input_string) == 0:
        raise ValueError("Input should be a non-empty string")

    return input_string[::2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_values_string('abcdef'), 'ace')

if __name__ == '__main__':
    unittest.main()