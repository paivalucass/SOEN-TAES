def tuple_str_int(test_str):
    import re
    try:
        pattern = r'\((\d+),\s*(\d+),\s*(\d+)\)'
        match = re.match(pattern, test_str)
        
        if match:
            result = tuple(map(int, match.groups()))
            return result
        else:
            return "Error: Invalid input format"
        
    except:
        return "Error: Missing closing parenthesis in input"

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_str_int("(7, 8, 9)"), (7, 8, 9))

if __name__ == '__main__':
    unittest.main()