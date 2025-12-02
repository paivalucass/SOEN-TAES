def extract_string(str_values, size):
    if not str_values:
        return []
    
    if size <= 0:
        return []
    
    result = [s for s in str_values if len(s) == size]
    if not result:
        raise ValueError("No strings of the specified size found in the input list")
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()