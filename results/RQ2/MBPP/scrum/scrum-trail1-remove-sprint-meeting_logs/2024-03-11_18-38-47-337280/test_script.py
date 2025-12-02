def string_to_tuple(input_string):
    try:
        if input_string == "":
            raise ValueError("Input string cannot be empty")
        tuple_of_characters = tuple(input_string)
        return tuple_of_characters
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_to_tuple('python 3.0'), ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0'))

if __name__ == '__main__':
    unittest.main()