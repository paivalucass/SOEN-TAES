def extract_string(input_list, specified_size):
    try:
        if not input_list:
            raise ValueError("Input list cannot be empty")
        if specified_size <= 0:
            raise ValueError("Specified size must be a positive integer")

        result = [string for string in input_list if len(string) == specified_size]
        return result

    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()