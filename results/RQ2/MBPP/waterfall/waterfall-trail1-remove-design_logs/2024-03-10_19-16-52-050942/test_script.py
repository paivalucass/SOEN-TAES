def extract_string(lst, length):
    if not isinstance(lst, list) or not isinstance(length, int) or length < 0:
        return "Invalid input"

    result = [s for s in lst if len(s) == length]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()