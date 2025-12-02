def string_to_tuple(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")

    return tuple(input_string)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple('python 3.0'), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()