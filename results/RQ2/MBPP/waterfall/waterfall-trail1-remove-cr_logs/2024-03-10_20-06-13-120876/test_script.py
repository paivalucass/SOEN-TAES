def extract_string(str_list, size):
    if not isinstance(str_list, list) or not all(isinstance(s, str) for s in str_list) or not isinstance(size, int) or size <= 0:
        raise ValueError("Invalid input. 'str_list' should be a list of string values and 'size' should be a positive integer.")

    extracted_strings = [s for s in str_list if len(s) == size]
    return extracted_strings
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()