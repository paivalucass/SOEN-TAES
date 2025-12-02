def count_distinct_characters(string: str) -> int:
    if not string:
        raise ValueError("Input string cannot be empty")
    
    lowercase_string = string.lower()
    distinct_characters = set(lowercase_string)
    distinct_characters.discard(' ')  # Remove spaces from distinct characters count
    return len(distinct_characters)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()