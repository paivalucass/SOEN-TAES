def extract_string(input_list, length):
    if not isinstance(input_list, list):
        return "Invalid input"
    
    result = [s for s in input_list if len(s) >= length]
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8), ['practice', 'solution'])

if __name__ == '__main__':
    unittest.main()