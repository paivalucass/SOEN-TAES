def extract_string(lst, l):
    result = [word for word in lst if len(word) >= l]
    return result

import unittest

class Test(unittest.TestCase):
    def test_extract_string(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()