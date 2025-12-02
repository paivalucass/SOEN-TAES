def is_lower(input_string):
    if isinstance(input_string, str):
        lower_string = input_string.lower()
        return lower_string
    else:
        raise ValueError("Input is not a string")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_lower('InValid'), 'invalid')

if __name__ == '__main__':
    unittest.main()