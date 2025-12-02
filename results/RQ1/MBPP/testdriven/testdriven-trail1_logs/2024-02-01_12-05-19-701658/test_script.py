def string_to_list(input_string):
    if input_string is None or input_string == "":
        raise ValueError("Input string cannot be empty or None")
    return input_string.split()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_list('python programming'), ['python', 'programming'])

if __name__ == '__main__':
    unittest.main()