def extract_string(str_list, size=0):
    if not isinstance(str_list, list) or size < 0:
        return "Invalid input"
    
    result = [s for s in str_list if isinstance(s, str) and len(s) == size]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()