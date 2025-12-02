def count_distinct_characters(string: str) -> int:
    string = string.lower()
    unique_chars = set(string)
    unique_chars = {char for char in unique_chars if char.isalnum()}
    return len(unique_chars)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

if __name__ == '__main__':
    unittest.main()