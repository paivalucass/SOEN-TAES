def extract_string(str_list, l):
    if not isinstance(str_list, list) or not isinstance(l, int) or l <= 0:
        return "Invalid input"
    
    result = [s for s in str_list if isinstance(s, str) and len(s) == l]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()