def extract_string(strings, size):
    if not isinstance(size, int) or size < 0:
        return "Size should be a non-negative integer"
    
    if not isinstance(strings, list) or len(strings) == 0:
        return "Strings should be a non-empty list"
    
    result = [string for string in strings if len(string) == size]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()