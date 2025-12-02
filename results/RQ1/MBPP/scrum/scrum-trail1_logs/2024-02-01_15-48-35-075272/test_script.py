def extract_string(strings, size):
    if not strings:
        return []
    if size <= 0:
        return []

    result = [s for s in strings if len(s) == size]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()