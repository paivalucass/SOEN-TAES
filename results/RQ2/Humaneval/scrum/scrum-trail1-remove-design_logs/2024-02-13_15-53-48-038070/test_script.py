def count_distinct_characters(string: str) -> int:
    if not string:
        raise ValueError("Input string cannot be empty or null")
    
    distinct_characters = set(string.lower())
    return len(distinct_characters)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()