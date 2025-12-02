def count_distinct_characters(string: str) -> int:
    char_count = {}
    
    for char in string:
        if char.lower() not in char_count:
            char_count[char.lower()] = 1
            
    return len(char_count)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()