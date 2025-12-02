def replace_spaces(string):
    if string is None or not isinstance(string, str):
        raise ValueError("Input must be a non-empty string")

    return '%20'.join(string.split())
import unittest

class Test(unittest.TestCase):
    def test_replace_spaces(self):
        self.assertEqual(replace_spaces("My Name is Dawood"), 'My%20Name%20is%20Dawood')

if __name__ == '__main__':
    unittest.main()