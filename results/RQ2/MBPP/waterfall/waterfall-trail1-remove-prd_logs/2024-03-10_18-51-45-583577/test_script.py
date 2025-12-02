def extract_string(input_list, length):
    if not isinstance(length, int) or length <= 0:
        return "Length should be a positive integer"

    result = [string for string in input_list if len(string) >= length]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()